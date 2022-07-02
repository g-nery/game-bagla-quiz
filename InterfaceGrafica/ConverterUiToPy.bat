md ../SourcePy
pyrcc5 Imagens/Resource.qrc -o ../SourcePy/Resource_rc.py
python -m PyQt5.uic.pyuic -x PrimeiraTela.ui -o ../SourcePy/PrimeiraTela.py
python -m PyQt5.uic.pyuic -x SegundaTela.ui -o ../SourcePy/SegundaTela.py
python -m PyQt5.uic.pyuic -x TerceiraTela.ui -o ../SourcePy/TerceiraTela.py
python -m PyQt5.uic.pyuic -x QuartaTela.ui -o ../SourcePy/QuartaTela.py
python -m PyQt5.uic.pyuic -x UltimaTela.ui -o ../SourcePy/UltimaTela.py