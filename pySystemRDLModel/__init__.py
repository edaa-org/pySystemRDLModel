# ==================================================================================================================== #
#              ____            _                 ____  ____  _     __  __           _      _                           #
#  _ __  _   _/ ___| _   _ ___| |_ ___ _ __ ___ |  _ \|  _ \| |   |  \/  | ___   __| | ___| |                          #
# | '_ \| | | \___ \| | | / __| __/ _ \ '_ ` _ \| |_) | | | | |   | |\/| |/ _ \ / _` |/ _ \ |                          #
# | |_) | |_| |___) | |_| \__ \ ||  __/ | | | | |  _ <| |_| | |___| |  | | (_) | (_| |  __/ |                          #
# | .__/ \__, |____/ \__, |___/\__\___|_| |_| |_|_| \_\____/|_____|_|  |_|\___/ \__,_|\___|_|                          #
# |_|    |___/       |___/                                                                                             #
# ==================================================================================================================== #
# Authors:                                                                                                             #
#   Patrick Lehmann                                                                                                    #
#                                                                                                                      #
# License:                                                                                                             #
# ==================================================================================================================== #
# Copyright 2023-2023 Patrick Lehmann - Boetzingen, Germany                                                            #
#                                                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                                                      #
# you may not use this file except in compliance with the License.                                                     #
# You may obtain a copy of the License at                                                                              #
#                                                                                                                      #
#   http://www.apache.org/licenses/LICENSE-2.0                                                                         #
#                                                                                                                      #
# Unless required by applicable law or agreed to in writing, software                                                  #
# distributed under the License is distributed on an "AS IS" BASIS,                                                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.                                             #
# See the License for the specific language governing permissions and                                                  #
# limitations under the License.                                                                                       #
#                                                                                                                      #
# SPDX-License-Identifier: Apache-2.0                                                                                  #
# ==================================================================================================================== #
#
"""
An abstract SystemRDL language model.

:copyright: Copyright 2023-2023 Patrick Lehmann - Bötzingen, Germany
:license: Apache License, Version 2.0
"""
from enum import unique, Enum
from typing import Dict, Union

from pyTooling.Decorators import export


__author__ =    "Patrick Lehmann"
__email__ =     "Paebbels@gmail.com"
__copyright__ = "2023-2023, Patrick Lehmann"
__license__ =   "Apache License, Version 2.0"
__version__ =   "0.2.1"


@export
@unique
class SystemRDLVersion(Enum):
	Any =             -1
	SystemRDL2005 = 2005
	SystemRDL2009 = 2009
	SystemRDL2012 = 2012
	SystemRDL2017 = 2017

	__VERSION_MAPPINGS__: Dict[Union[int, str], Enum] = {
		-1:     Any,
		5:      SystemRDL2005,
		9:      SystemRDL2009,
		12:     SystemRDL2012,
		17:     SystemRDL2017,
		2005:   SystemRDL2005,
		2009:   SystemRDL2009,
		2012:   SystemRDL2012,
		2017:   SystemRDL2017,
		"Any":  Any,
		"05":   SystemRDL2005,
		"09":   SystemRDL2009,
		"12":   SystemRDL2012,
		"17":   SystemRDL2017,
		"2005": SystemRDL2005,
		"2009": SystemRDL2009,
		"2012": SystemRDL2012,
		"2017": SystemRDL2017,
	}

	def __init__(self, *_):
		"""Patch the embedded MAP dictionary"""
		cls = self.__class__
		for k, v in cls.__VERSION_MAPPINGS__.items():
			if (not isinstance(v, cls)) and (v == self.value):
				cls.__VERSION_MAPPINGS__[k] = self

	@classmethod
	def Parse(cls, value: Union[int, str]) -> "SystemRDLVersion":
		try:
			return cls.__VERSION_MAPPINGS__[value]
		except KeyError:
			raise ValueError(f"Value '{value!s}' cannot be parsed to member of {cls.__name__}.")

	def __lt__(self, other):
		return self.value < other.value

	def __le__(self, other):
		return self.value <= other.value

	def __gt__(self, other):
		return self.value > other.value

	def __ge__(self, other):
		return self.value >= other.value

	def __ne__(self, other):
		return self.value != other.value

	def __eq__(self, other):
		if (self is self.__class__.Any) or (other is self.__class__.Any):
			return True
		else:
			return self.value == other.value

	def __str__(self) -> str:
		if self.value == -1:
			return "SystemRDL'Any"
		else:
			return f"SystemRDL'{str(self.value)[-2:]}"

	def __repr__(self) -> str:
		if self.value == -1:
			return "Any"
		else:
			return str(self.value)
