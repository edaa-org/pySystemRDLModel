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
"""Package installer for 'An abstract SystemRDL language model'."""
from pathlib             import Path
from pyTooling.Packaging import DescribePythonPackageHostedOnGitHub, DEFAULT_CLASSIFIERS

gitHubNamespace =        "edaa-org"
packageName =            "pySystemRDLModel"
packageDirectory =       packageName
packageInformationFile = Path(f"{packageDirectory}/__init__.py")

DescribePythonPackageHostedOnGitHub(
	packageName=packageName,
	description="An abstract SystemRDL language model.",
	gitHubNamespace=gitHubNamespace,
	keywords="Python3 SystemRDL Language Model Abstract",
	sourceFileWithVersion=packageInformationFile,
	developmentStatus="alpha",
	classifiers=list(DEFAULT_CLASSIFIERS) + [
		"Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
		"Topic :: Software Development :: Code Generators",
		"Topic :: Software Development :: Compilers"
	]
)
