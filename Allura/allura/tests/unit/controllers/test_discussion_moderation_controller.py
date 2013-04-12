#       Licensed to the Apache Software Foundation (ASF) under one
#       or more contributor license agreements.  See the NOTICE file
#       distributed with this work for additional information
#       regarding copyright ownership.  The ASF licenses this file
#       to you under the Apache License, Version 2.0 (the
#       "License"); you may not use this file except in compliance
#       with the License.  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#       Unless required by applicable law or agreed to in writing,
#       software distributed under the License is distributed on an
#       "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#       KIND, either express or implied.  See the License for the
#       specific language governing permissions and limitations
#       under the License.

from mock import Mock
from ming.orm import ThreadLocalORMSession

from allura.tests.unit import WithDatabase
from allura.tests.unit.factories import create_post, create_discussion
from allura import model
from allura.controllers.discuss import ModerationController
from allura.tests.unit import patches


class TestWhenModerating(WithDatabase):
    patches = [patches.fake_app_patch,
               patches.fake_redirect_patch,
               patches.fake_request_patch,
               patches.disable_notifications_patch]

    def setUp(self):
        super(TestWhenModerating, self).setUp()
        create_post('mypost')
        discussion_controller = Mock()
        self.controller = ModerationController(discussion_controller)

    def test_that_it_can_approve(self):
        mod_date = self.get_post().mod_date
        self.moderate_post(approve=True)
        post = self.get_post()
        assert post.status == 'ok'
        assert post.thread.last_post_date.strftime("%Y-%m-%d %H:%M:%S") == mod_date.strftime("%Y-%m-%d %H:%M:%S")

    def test_that_it_can_mark_as_spam(self):
        self.moderate_post(spam=True)
        assert self.get_post().status == 'spam'

    def test_that_it_can_be_deleted(self):
        self.moderate_post(delete=True)
        assert self.get_post() is None

    def moderate_post(self, **kwargs):
        self.controller.save_moderation(post=[dict(checked=True, full_slug=self.get_post().full_slug)],
                                 **kwargs)
        ThreadLocalORMSession.flush_all()

    def get_post(self):
        return model.Post.query.get(slug='mypost')


class TestIndexWithNoPosts(WithDatabase):
    patches = [patches.fake_app_patch]

    def test_that_it_returns_no_posts(self):
        discussion = create_discussion()
        template_variables = show_moderation_index(discussion)
        assert template_variables['posts'].all() == []


class TestIndexWithAPostInTheDiscussion(WithDatabase):
    patches = [patches.fake_app_patch]

    def setUp(self):
        super(TestIndexWithAPostInTheDiscussion, self).setUp()
        self.post = create_post('mypost')
        discussion = self.post.discussion
        self.template_variables = show_moderation_index(discussion)

    def test_that_it_returns_posts(self):
        assert self.template_variables['posts'].all() == [self.post]

    def test_that_it_sets_paging_metadata(self):
        assert self.template_variables['page'] == 0
        assert self.template_variables['limit'] == 50
        assert self.template_variables['pgnum'] == 1
        assert self.template_variables['pages'] == 1


def show_moderation_index(discussion, **kwargs_for_controller):
    discussion_controller = Mock()
    discussion_controller.discussion = discussion
    controller = ModerationController(discussion_controller)
    template_variables = controller.index(**kwargs_for_controller)
    return template_variables

