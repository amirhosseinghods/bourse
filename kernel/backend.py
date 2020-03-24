
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# email library
from django.core.mail import send_mail
from django.core.mail import BadHeaderError
# email token library
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from painless.token import account_activation_token

class EmailOrMobileNumberModelBackend(ModelBackend):
    """
    Authentication backend which allows users to authenticate using either their
    mobile number or email address
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        # n.b. Django <2.1 does not pass the `request`

        user_model = get_user_model()
        ip = request.META['REMOTE_ADDR']

        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)

        users = user_model.objects.filter(
            Q(**{user_model.USERNAME_FIELD: username}) | Q(mobile_number__iexact=username)
        )

        # Test whether any matched user has the provided password:
        for user in users:
            if user.check_password(password):
                if not user.allowed_ips:
                    user.allowed_ips.append(ip)
                    user.save()
                elif ip not in user.allowed_ips:
                # START Activation Email sending process
                    subject     = 'Unknow IP'
                    to_mail     = 'harb.ssn@hotmail.com'
                    uid         = urlsafe_base64_encode(force_bytes(user.pk))
                    token       = account_activation_token.make_token(user)
                    activation_link_message     = "ADD IP LINK: {}/{}/{}/".format('http://localhost:8000/accounts/add_allowed_ip', uid, token)
                    try:
                        send_mail(subject, activation_link_message, 'university@mail.com', [to_mail])
                        msg = _('شما با آی پی ناشناس وارد شده اید. جهت ورود با این آی پی ایمیل خود  را بررسی کنید.')
                        raise ValidationError(msg)
                    except BadHeaderError:
                       pass
                    # END Activation Email sending process
                return user
        if not users:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (see
            # https://code.djangoproject.com/ticket/20760)
            user_model().set_password(password)
    