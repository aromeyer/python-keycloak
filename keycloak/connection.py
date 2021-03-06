# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Marcos Pereira <marcospereira.mpj@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

from .exceptions import *
import requests


class ConnectionManager(object):
    """ Represents a simple server connection.
    Args:
        base_url (str): The server URL.
        headers (dict): The header parameters of the requests to the server.
        timeout (int): Timeout to use for requests to the server.
    """

    def __init__(self, base_url, headers={}, timeout=60):
        self.__base_url = base_url
        self.__headers = headers
        self.__timeout = timeout

    def get_url(self):
        """ Return base url in use for requests to the server. """
        return self.__base_url

    def get_timeout(self):
        """ Return timeout in use for request to the server. """
        return self.__timeout

    def set_headers(self, params):
        """ Update header request to the server.
        :arg
            params (dict): Parameters header request.
        """
        self.__headers = params

    def get_headers(self):
        """ Return header request to the server. """
        return self.__headers

    def get_param_headers(self, key):
        """ Return a specific header parameter.
        :arg
            key (str): Header parameters key.
        :return:
            If the header parameters exist, return its value.
        """
        return self.__headers.get(key)

    def clean_headers(self):
        """ Clear header parameters. """
        self.__headers = {}

    def exist_param_headers(self, key):
        """ Check if the parameter exists in the header.
        :arg
            key (str): Header parameters key.
        :return:
            If the header parameters exist, return True.
        """
        return self.get_param_headers(key) is not None

    def add_param_headers(self, key, value):
        """ Add a single parameter inside the header.
        :arg
            key (str): Header parameters key.
            value (str): Value to be added.
        """
        self.__headers[key] = value

    def del_param_headers(self, key):
        """ Remove a specific parameter.
        :arg
            key (str): Key of the header parameters.
        """
        self.__headers.pop(key, None)

    def raw_get(self, path, **kwargs):
        """ Submit get request to the path.
        :arg
            path (str): Path for request.
        :return
            Response the request.
        :exception
            HttpError: Can't connect to server.
        """

        try:
            return requests.get(urljoin(self.get_url(), path),
                                params=kwargs,
                                headers=self.get_headers(),
                                timeout=self.get_timeout())
        except Exception as e:
            raise KeycloakConnectionError(
                "Can't connect to server (%s)" % e)

    def raw_post(self, path, data, **kwargs):
        """ Submit post request to the path.
        :arg
            path (str): Path for request.
            data (dict): Payload for request.
        :return
            Response the request.
        :exception
            HttpError: Can't connect to server.
        """
        try:
            return requests.post(urljoin(self.get_url(), path),
                                 params=kwargs,
                                 data=data,
                                 headers=self.get_headers(),
                                 timeout=self.get_timeout())
        except Exception as e:
            raise KeycloakConnectionError(
                "Can't connect to server (%s)" % e)

    def raw_put(self, path, data, **kwargs):
        """ Submit put request to the path.
        :arg
            path (str): Path for request.
            data (dict): Payload for request.
        :return
            Response the request.
        :exception
            HttpError: Can't connect to server.
        """
        try:
            return requests.put(urljoin(self.get_url(), path),
                                params=kwargs,
                                data=data,
                                headers=self.get_headers(),
                                timeout=self.get_timeout())
        except Exception as e:
            raise KeycloakConnectionError(
                "Can't connect to server (%s)" % e)
