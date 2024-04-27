from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated

# Email Verification
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage

@user_not_authenticated
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            if email:
                username = email.split('@')[0]
                password = form.cleaned_data['password']
                user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                user.phone_number = phone_number
                user.save()

                # USER ACCOUNT ACTIVATION
                current_site = get_current_site(request)
                mail_subject = 'Please activate your greatkart account'
                message = render_to_string('accounts/account_verification_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user), 
                })
                to_email = [email]  # Make sure to_email is a list
                send_email = EmailMessage(mail_subject, message, to=to_email)
                try:
                    send_email.send()
                    # messages.success(request, 'Please check your email to activate your account.')
                except Exception as e:
                    return HttpResponse("Email sending failed: " + str(e))
                return redirect('/accounts/login/?command=verification&email='+email)
            else:
                messages.error(request, 'Email is required.')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

@user_not_authenticated
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user:
            auth.login(request, user)
            # messages.success(request, 'You are now logged in')
            return redirect('home:home')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('accounts:login')
    return render(request, 'accounts/login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('accounts:login')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated!')
        return redirect('accounts:login')
    else:
        messages.error(request, 'Invalid activation link!')
        return redirect('accounts:register')

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')