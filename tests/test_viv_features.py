# Copyright (C) 2023 Mandiant, Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
# You may obtain a copy of the License at: [package root]/LICENSE.txt
# Unless required by applicable law or agreed to in writing, software distributed under the License
#  is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.
import fixtures
from fixtures import scope, sample


@fixtures.parametrize(
    "sample,scope,feature,expected",
    fixtures.FEATURE_PRESENCE_TESTS + fixtures.FEATURE_SYMTAB_FUNC_TESTS,
    indirect=["sample", "scope"],
)
def test_viv_features(sample, scope, feature, expected):
    fixtures.do_test_feature_presence(fixtures.get_viv_extractor, sample, scope, feature, expected)


@fixtures.parametrize(
    "sample,scope,feature,expected",
    fixtures.FEATURE_COUNT_TESTS,
    indirect=["sample", "scope"],
)
def test_viv_feature_counts(sample, scope, feature, expected):
    fixtures.do_test_feature_count(fixtures.get_viv_extractor, sample, scope, feature, expected)
