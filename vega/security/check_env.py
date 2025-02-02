# -*- coding:utf-8 -*-

# Copyright (C) 2020. Huawei Technologies Co., Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Check security env."""

import vega


__all__ = ["check_env"]


def check_env(config) -> bool:
    """Check security env."""
    if vega.is_tf_backend():
        print("Vega can not run on TensorFlow in the security model.")
        return False
    pipeline = config.get("pipeline", [])
    for step in pipeline:
        if step in config:
            if config[step]["pipe_step"]["type"] == "HorovodTrainStep":
                print("Vega can not run on Horovod in the security model.")
                return False
    return True
