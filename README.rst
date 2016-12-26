SaKKe  :gift:
==============

SaKKe est un utilitaire simple de génération de statistiques de devoirs.

Installation
-------------


.. code-block:: bash

  [sudo] pip install sakke [--user]

Usage et hypothèses
----------------------

Afficher l'aide : 

.. code-block:: bash

  sakke --help

Les questions des exercices sont notées par défaut sur 4.
Un fichier de barème ajuste la note finale.

.. code-block:: bash

  sakke exercice_1:bareme_1 exercice_2:bareme_2 ...

* exercice est un fichier csv : 

.. code-block:: none

  nom1, prenom1, note11, note12,...
  nom2, prenom2, note21, note22,...


* bareme est un fichier csv : 

.. code-block:: none

   intitule1, intitule2, ...
   bareme1, bareme2, ...

Sortie
-------

Un fichier  :code:`out.tex` compilable avec pdflatex.
