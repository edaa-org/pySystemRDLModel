.. _GLOSSARY:

Glossary
########

.. glossary::

   Accellera
   Accellera Systems Initiative
     `Accellera Systems Initiative <https://www.accellera.org/>`__ is the standards organization of the electronic
     design automation industry, formed from Open Verilog International (OVI) and VHDL International, later joined by
     :term:`The SPIRIT Consortium <SPIRIT>` and the Open SystemC Initiative (OSCI).

     Accellera publishes :term:`SystemRDL`.

   IP-XACT
     An XML format describing electronic components and their designs (IP), standardized as IEEE Std. 1685. A
     :term:`SystemRDL` description can be a source of IP-XACT descriptions.

     Wikipedia: :wiki:`IP-XACT`

   LRM
   Language Reference Manual
     The standard defining a language's syntax and semantics. For :term:`SystemRDL`, Accellera's
     `SystemRDL download page <https://accellera.org/downloads/standards/systemrdl>`__ provides:

     * `SystemRDL 2.0 <https://accellera.org/images/downloads/standards/systemrdl/SystemRDL_2.0_Jan2018.pdf>`__
       (January 2018).
     * SystemRDL 1.0 (previous release, 2009).

   SPIRIT
   The SPIRIT Consortium
     The consortium that created :term:`IP-XACT` and released :term:`SystemRDL` 1.0 in 2009. It merged with the
     :term:`Accellera` Organization, which took over both.

   SystemRDL
   Register Description Language
     A language describing the registers and memory maps of a design: address maps, register files, registers and
     fields. It is a single source for the register description, from which all views - RTL code, documentation,
     verification models or :term:`IP-XACT` descriptions - can be generated. Published by :term:`Accellera` (see
     :term:`LRM`).

     pySystemRDLModel names the language revisions in :class:`~pySystemRDLModel.SystemRDLVersion`.

     Wikipedia: :wiki:`SystemRDL`
