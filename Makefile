all: album.pdf check

check: album.pdf
	pdfimages -list album.pdf | tail -n +3 | awk '{print $$1 " " $$13}' | while read page ppi; do test 0"$$ppi" -lt 250 && echo page $${page}: $${ppi} ppi; done; true

photos-cmyk:
	mkdir -p photos.cmyk
	convert couverture-rgb.jpg -colorspace cmyk -profile PSOcoated_v3.icc couverture-cmyk.jpg
	cd photos.rgb; for i in *.*; do test "$$i" -nt "../photos.cmyk/$$i" && convert "$$i" -resize 1900x1900 -colorspace cmyk -profile ../PSOcoated_v3.icc "../photos.cmyk/$$i" && echo -n .; done; echo; true
	cd photos.cmyk; for i in *; do test -e "../photos.rgb/$$i" || rm "$$i"; done

photos.tex: photos.py photos-cmyk
	python2 photos.py > photos.tex

album.pdf: album.tex photos.tex
	xelatex album.tex
