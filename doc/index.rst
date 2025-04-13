.. include:: shields.inc

.. image:: _static/logo.svg
   :height: 90 px
   :align: center
   :target: https://GitHub.com/edaa-org/pySystemRDLModel

.. raw:: html

    <br>

.. raw:: latex

   \part{Introduction}

.. only:: html

   |  |SHIELD:svg:pySystemRDLModel-github| |SHIELD:svg:pySystemRDLModel-src-license| |SHIELD:svg:pySystemRDLModel-ghp-doc| |SHIELD:svg:pySystemRDLModel-doc-license| |SHIELD:svg:pySystemRDLModel-gitter|
   |  |SHIELD:svg:pySystemRDLModel-pypi-tag| |SHIELD:svg:pySystemRDLModel-pypi-status| |SHIELD:svg:pySystemRDLModel-pypi-python|
   |  |SHIELD:svg:pySystemRDLModel-gha-test| |SHIELD:svg:pySystemRDLModel-lib-status| |SHIELD:svg:pySystemRDLModel-codacy-quality| |SHIELD:svg:pySystemRDLModel-codacy-coverage| |SHIELD:svg:pySystemRDLModel-codecov-coverage|

.. Disabled shields: |SHIELD:svg:pySystemRDLModel-lib-dep| |SHIELD:svg:pySystemRDLModel-req-status| |SHIELD:svg:pySystemRDLModel-lib-rank|

.. only:: latex

   |SHIELD:png:pySystemRDLModel-github| |SHIELD:png:pySystemRDLModel-src-license| |SHIELD:png:pySystemRDLModel-ghp-doc| |SHIELD:png:pySystemRDLModel-doc-license| |SHIELD:png:pySystemRDLModel-gitter|
   |SHIELD:png:pySystemRDLModel-pypi-tag| |SHIELD:png:pySystemRDLModel-pypi-status| |SHIELD:png:pySystemRDLModel-pypi-python|
   |SHIELD:png:pySystemRDLModel-gha-test| |SHIELD:png:pySystemRDLModel-lib-status| |SHIELD:png:pySystemRDLModel-codacy-quality| |SHIELD:png:pySystemRDLModel-codacy-coverage| |SHIELD:png:pySystemRDLModel-codecov-coverage|

.. Disabled shields: |SHIELD:png:pySystemRDLModel-lib-dep| |SHIELD:png:pySystemRDLModel-req-status| |SHIELD:png:pySystemRDLModel-lib-rank|

The pySystemRDLModel Documentation
##################################

An abstract SystemRDL language model.


.. _GOALS:

Main Goals
**********

This package provides a unified abstract language model for SystemRDL.
Projects reading from source files can derive own classes and implement additional logic to create a concrete language
model for their tools.

Projects consuming pre-processed SystemRDL data (parsed, analyzed or elaborated) can build higher level features
and services on such a model, while supporting multiple frontends.


.. _USECASES:

Use Cases
*********

* TBD


.. _NEWS:

News
****

.. only:: html

   June 2023 - New Repository Created
   ==================================

.. only:: latex

   .. rubric:: New Repository Created

* Moved ``SystemRDLVersion`` class from ``pyEDAA.ProjectModel`` to this new repository.


.. _CONTRIBUTORS:

Contributors
************

* :gh:`Patrick Lehmann <Paebbels>` (Maintainer)
* `and more... <https://GitHub.com/edaa-org/pySystemRDLModel/graphs/contributors>`__


.. _LICENSE:

License
*******

.. only:: html

   This Python package (source code) is licensed under `Apache License 2.0 <Code-License.html>`__. |br|
   The accompanying documentation is licensed under `Creative Commons - Attribution 4.0 (CC-BY 4.0) <Doc-License.html>`__.

.. only:: latex

   This Python package (source code) is licensed under **Apache License 2.0**. |br|
   The accompanying documentation is licensed under **Creative Commons - Attribution 4.0 (CC-BY 4.0)**.


.. toctree::
   :hidden:

   Used as a layer of EDA² ➚ <https://edaa-org.github.io/>

.. toctree::
   :caption: Introduction
   :hidden:

   Installation
   Dependency

.. raw:: latex

   \part{Main Documentation}

.. toctree::
   :caption: Main Documentation
   :hidden:

   LanguageModel/index


.. raw:: latex

   \part{References and Reports}

.. toctree::
   :caption: References and Reports
   :hidden:

   Python Class Reference <pySystemRDLModel/pySystemRDLModel>
   unittests/index
   coverage/index
   Doc. Coverage Report <DocCoverage>
   Static Type Check Report ➚ <typing/index>

.. raw:: latex

   \part{Appendix}

.. toctree::
   :caption: Appendix
   :hidden:

   License
   Doc-License
   Glossary
   genindex
   Python Module Index <modindex>
   TODO
