import re


class LinksChecker:
    regex_for_links = "%s.+\\(https.+?applicationId(=|%s)%d.+?\\)"

    @staticmethod
    def contains_link_for_product_and_os(email, os, app_id):
        desired_line = LinksChecker.regex_for_links % (os, "%253D", app_id)
        if re.search(desired_line, email) is None:
            return False
        else:
            return True
