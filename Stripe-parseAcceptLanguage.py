# -*- coding: utf-8 -*-
# Part 1
# In an HTTP request, the Accept-Language header describes the list of
# languages that the requester would like content to be returned in. The header
# takes the form of a comma-separated list of language tags. For example:
#   Accept-Language: en-US, fr-CA, fr-FR
# means that the reader would accept:
#   1. English as spoken in the United States (most preferred)
#   2. French as spoken in Canada
#   3. French as spoken in France (least preferred)
# We're writing a server that needs to return content in an acceptable language
# for the requester, and we want to make use of this header. Our server doesn't
# support every possible language that might be requested (yet!), but there is a
# set of languages that we do support. Write a function that receives two arguments:
# an Accept-Language header value as a string and a set of supported languages,
# and returns the list of language tags that will work for the request. The
# language tags should be returned in descending order of preference (the
# same order as they appeared in the header).
# In addition to writing this function, you should use tests to demonstrate that it's
# correct, either via an existing testing system or one you create.
# Examples:
# parse_accept_language(
#   "en-US, fr-CA, fr-FR",  # the client's Accept-Language header, a string
#   ["fr-FR", "en-US"]      # the server's supported languages, a set of strings
# )
# returns: ["en-US", "fr-FR"]
# parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"])
# returns: ["fr-FR"]
# parse_accept_language("en-US", ["en-US", "fr-CA"])
# returns: ["en-US"]
# Part 2
# Accept-Language headers will often also include a language tag that is not
# region-specific - for example, a tag of "en" means "any variant of English". Extend
# your function to support these language tags by letting them match all specific
# variants of the language.
# Examples:
# parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"])
# returns: ["en-US"]
# parse_accept_language("fr", ["en-US", "fr-CA", "fr-FR"])
# returns: ["fr-CA", "fr-FR"]
# parse_accept_language("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"])
# returns: ["fr-FR", "fr-CA"]
# Part 3
# Accept-Language headers will sometimes include a "wildcard" entry, represented
# by an asterisk, which means "all other languages". Extend your function to
# support the wildcard entry.
# Examples:
# parse_accept_language("en-US, *", ["en-US", "fr-CA", "fr-FR"])
# returns: ["en-US", "fr-CA", "fr-FR"]
# parse_accept_language("fr-FR, fr, *", ["en-US", "fr-CA", "fr-FR"])
# returns: ["fr-FR", "fr-CA", "en-US"]
# Part 4
# Accept-Language headers will sometimes include explicit numeric weights (known as
# q-factors) for their entries, which are used to designate certain language tags
# as specifically undesired. For example:
# Accept-Language: fr-FR;q=1, fr;q=0.5, fr-CA;q=0
# This means that the reader most prefers French as spoken in France, will take
# any variant of French after that, but specifically wants French as spoken in
# Canada only as a last resort. Extend your function to parse and respect q-factors.
# Examples:
# parse_accept_language("fr-FR;q=1, fr-CA;q=0, fr;q=0.5", ["fr-FR", "fr-CA", "fr-BG"])
# returns: ["fr-FR", "fr-BG", "fr-CA"]
# parse_accept_language("fr-FR;q=1, fr-CA;q=0, *;q=0.5", ["fr-FR", "fr-CA", "fr-BG", "en-US"])
# returns: ["fr-FR", "fr-BG", "en-US", "fr-CA"]
# parse_accept_language("fr-FR;q=1, fr-CA;q=0.8, *;q=0.5", ["fr-FR", "fr-CA", "fr-BG", "en-US"])

class Solution(object):
    def parseAcceptLanguagePart4(self, accepts, supports):
        # {1 => {"fr" => ["fr-FR", "fr-CA"]}}
        dic = {}
        dic[1] = {"fr": ["fr-FR", "fr-CA"]}
        dic[0] = {"en": ["en-US", "en-CA"]}

        visited = set()
        res = []
        for k, v in sorted(dic.items(), reverse=True):
            for r_list in v.values():
                for r in r_list:
                    if r not in visited:
                        visited.add(r)
                        res.append(r)
        return res

    def parseAcceptLanguage(self, accepts, supports):
        res = set()
        accepts = accepts.split(', ')
        for a in accepts:
            if '-' in a:
                for s in supports:
                    if a == s:
                        res.add(s)
            # Part 3
            elif a == '*':
                return supports
            else:
                for s in supports:
                    curr = s.split('-')
                    if a == curr[0]:
                        res.add(s)
        return list(res)

test = Solution()
print test.parseAcceptLanguagePart4("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"])