from abc import ABC, abstractmethod


class Website:
    def __init__(self, implementation):
        self._implementation = implementation

    def showPage(self):
        pass


class Implementation(ABC):

    def show_articles(self):
        return "article"

    def show_ads(self):
        return "ads for the user"

    @abstractmethod
    def call_to_action(self):
        pass


class FreeUser(Implementation):

    def call_to_action(self):
        return "pay 10$ to remove ads "


class FreeWebsite(Website):

    def showPage(self):
        get_article = self._implementation.show_articles()
        get_ads = self._implementation.show_ads()

        print(get_ads, get_article)



class PaidWesite(Website):

    def showPage(self):
        get_articles = self._implementation.show_articles()
        print(get_articles)

    def rgnrg(self):
        print("trsting")


# c= Implementation()
# print(c.call_to_action())
free = FreeWebsite(FreeUser())
paid= PaidWesite(FreeUser())
paid.rgnrg()
