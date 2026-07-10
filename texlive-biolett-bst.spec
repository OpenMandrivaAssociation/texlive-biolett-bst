%global tl_name biolett-bst
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A BibTeX style for the journal Biology Letters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/biolett-bst
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biolett-bst.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biolett-bst.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a BibTeX style (.bst) file for the journal
"Biology Letters" published by the Royal Society. This style was
produced independently and hence has no formal approval from the Royal
Society.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/bibtex
%dir %{_datadir}/texmf-dist/bibtex/bst/biolett-bst
%dir %{_datadir}/texmf-dist/doc/bibtex/biolett-bst
%{_datadir}/texmf-dist/bibtex/bst/biolett-bst/biolett.bst
%doc %{_datadir}/texmf-dist/doc/bibtex/biolett-bst/README.txt
