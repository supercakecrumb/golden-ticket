# lucky-ticket

Всё началось с того, что старые советские троллейбусные билетики заменили на чеки со штрихкодами... Сайт был написан из чистейших побуждений упростить расчет счастливого билетика для жителей Петрозаводска. [Сам сайт](https://lucky-ticket.brand-shoot.ru)
## Deployment signing key

Before deploying, provision a unique random `SECRET_KEY` (at least 32 characters) using the deployment secret store. Startup fails closed without it. Replacing the previous shared default invalidates existing Flask sessions. Ticket inputs are not logged.
