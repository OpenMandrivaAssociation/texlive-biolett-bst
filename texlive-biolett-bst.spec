Name:		texlive-biolett-bst
Version:	66115
Release:	1
Summary:	A BibTeX style for the journal "Biology Letters"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biolett-bst
License:	lppl1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biolett-bst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biolett-bst.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a BibTeX style (.bst) file for the
journal "Biology Letters" published by the Royal Society. This
style was produced independently and hence has no formal
approval from the Royal Society.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/biolett-bst
%doc %{_texmfdistdir}/doc/bibtex/biolett-bst

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
