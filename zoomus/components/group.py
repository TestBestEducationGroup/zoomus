"""Zoom.us REST API Python Client -- group component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components import base


class GroupComponent(base.BaseComponent):
    """Component dealing with all group related matters"""

    def list(self, **kwargs):
        return self.post_request("/group/list", params=kwargs)

    def create(self, **kwargs):
        return self.post_request("/group/create", params=kwargs)

    def edit(self, **kwargs):
        util.require_keys(kwargs, 'id')
        return self.post_request("/group/edit", params=kwargs)

    def delete(self, **kwargs):
        util.require_keys(kwargs, 'id')
        return self.post_request("/group/delete", params=kwargs)

    def get(self, **kwargs):
        util.require_keys(kwargs, 'id')
        return self.post_request("/group/get", params=kwargs)

    def member_add(self, **kwargs):
        util.require_keys(kwargs, ['id', 'member_ids'])
        return self.post_request("/group/member/add", params=kwargs)

    def member_delete(self, **kwargs):
        util.require_keys(kwargs, ['id', 'member_ids'])
        return self.post_request("/group/member/delete", params=kwargs)

    def member_list(self, **kwargs):
        util.require_keys(kwargs, 'id')
        return self.post_request("/group/member/list", params=kwargs)


class GroupComponentV2(base.BaseComponent):
    def list(self, **kwargs):
        return self.get_request("/groups", params=kwargs)

    def create(self, **kwargs):
        return self.post_request("/groups", data=kwargs)

    def update(self, **kwargs):
        util.require_keys(kwargs, ['id', 'data'])
        return self.patch_request(
            "/groups/{}".format(kwargs.get('id')),
            data=kwargs.get['data'])

    def delete(self, **kwargs):
        util.require_keys(kwargs, 'id')
        return self.delete_request(
            "/groups/{}".format(kwargs.get('id')),
            params=kwargs)

    def retrieve(self, **kwargs):
        util.require_keys(kwargs, 'id')
        return self.get_request(
            "/groups/{}".format(kwargs.get('id')),
            params=kwargs)

    def member_add(self, **kwargs):
        util.require_keys(kwargs, ['id', 'members'])
        return self.post_request(
            "/group/{}/members".format(kwargs.get('id')),
             params=kwargs)

    def member_delete(self, **kwargs):
        util.require_keys(kwargs, ['id', 'members'])
        return self.delete_request(
            "/group/{}/members".format(kwargs.get('id')),
             params=kwargs)

    def member_list(self, **kwargs):
        util.require_keys(kwargs, 'id')
        return self.post_request(
            "/group/{}/members".format(kwargs.get('id')),
             params=kwargs)
