# -*- coding: UTF-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Domain
from .serializers import DiffSerializer#, PageSerializer

import html2text

import difflib
import requests
import urlparse
import json

RESP = {
    "meta": {
        "has_diff": False,
        "num_diff": 0,
    },
    "diff": None
}

class PageDiffOrCreate(APIView):
    """
    View to compare the passed in uri with our current value if
    it exists

    http://pymotw.com/2/difflib/

    """

    def post(self, request, format=None):
        """
        compare page with domain
        """
        resp = RESP.copy()
        try:
            uri = json.loads(request.body)
            uri = uri.get('uri')

        except:
            try:
                uri = request.POST['uri']

            except:
                raise Exception('You must post a uri paramter: uri=>http://www.google.co.uk/intl/en/policies/terms/regional.html or {"uri": "http://www.google.co.uk/intl/en/policies/terms/regional.html"}')


        url = urlparse.urlparse(uri)

        domain, is_new = Domain.objects.get_or_create(domain=url.netloc)

        page = domain.page_set.filter(part=url.path).first()

        r = requests.get(uri)
        diff = []

        if r.status_code in [200]:
            h = html2text.HTML2Text()
            h.ignore_links = True
            current_body = h.handle(r.content)
        
            if page is None:
                page = domain.page_set.create(part=url.path, body=current_body)

            else:
                #
                # compare current with previous
                #
                
                differentials = list(difflib.unified_diff(current_body.splitlines(), page.body.splitlines(), lineterm=''))
                diff = '\n'.join(differentials)

                if diff:
                    # more than 0 diff
                    page = domain.page_set.create(part=url.path, body=current_body)
                    resp.update({
                        "meta": {
                            "has_diff": True,
                            "num_diff": len(differentials),
                        },
                        "diff": diff
                    })


        return Response(resp)