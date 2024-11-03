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
# Copyright 2023-2024 Patrick Lehmann - Boetzingen, Germany                                                            #
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
"""Instantiation tests for the language model."""
from unittest import TestCase

from pySystemRDLModel import SystemRDLVersion


if __name__ == "__main__": # pragma: no cover
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class SysRDLVersion(TestCase):
	def test_Any(self) -> None:
		versions = (
			SystemRDLVersion.Parse(-1),
			SystemRDLVersion.Parse("Any"),
		)

		for version in versions:
			self.assertIs(SystemRDLVersion.Any, version)

		print()
		print(version)
		print(version.value)

	def test_2005(self) -> None:
		versions = (
			SystemRDLVersion.Parse(5),
			SystemRDLVersion.Parse(2005),
			SystemRDLVersion.Parse("05"),
			SystemRDLVersion.Parse("2005"),
		)

		for version in versions:
			self.assertIs(SystemRDLVersion.SystemRDL2005, version)

		print()
		print(version)
		print(version.value)

	def test_2009(self) -> None:
		versions = (
			SystemRDLVersion.Parse(9),
			SystemRDLVersion.Parse(2009),
			SystemRDLVersion.Parse("09"),
			SystemRDLVersion.Parse("2009"),
		)

		for version in versions:
			self.assertIs(SystemRDLVersion.SystemRDL2009, version)

		print()
		print(version)
		print(version.value)

	def test_2012(self) -> None:
		versions = (
			SystemRDLVersion.Parse(12),
			SystemRDLVersion.Parse(2012),
			SystemRDLVersion.Parse("12"),
			SystemRDLVersion.Parse("2012"),
		)

		for version in versions:
			self.assertIs(SystemRDLVersion.SystemRDL2012, version)

		print()
		print(version)
		print(version.value)

	def test_2017(self) -> None:
		versions = (
			SystemRDLVersion.Parse(17),
			SystemRDLVersion.Parse(2017),
			SystemRDLVersion.Parse("17"),
			SystemRDLVersion.Parse("2017"),
		)

		for version in versions:
			self.assertIs(SystemRDLVersion.SystemRDL2017, version)

		print()
		print(version)
		print(version.value)

	def test_IntError(self) -> None:
		with self.assertRaises(ValueError):
			_ = SystemRDLVersion.Parse(0)

		with self.assertRaises(ValueError):
			_ = SystemRDLVersion.Parse(13)

	def test_StrError(self) -> None:
		with self.assertRaises(ValueError):
			_ = SystemRDLVersion.Parse("0")

		with self.assertRaises(ValueError):
			_ = SystemRDLVersion.Parse("13")
