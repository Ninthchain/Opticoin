from tempmail import TempMail


class Mail:
    mail : TempMail

    def __int__(self, login: str, domain: str):
        if domain is None:
            domain = ""
        if domain is None:
            raise Exception
        mail = TempMail(domain=domain)


class MailGenerator:
    domain: str

    def __int__(self, domain: str):
        self.domain = domain

    def generate(self) -> str:
        raise NotImplementedError
