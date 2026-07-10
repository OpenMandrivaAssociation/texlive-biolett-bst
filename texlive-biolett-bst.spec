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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a BibTeX style (.bst) file for the journal
"Biology Letters" published by the Royal Society. This style was
produced independently and hence has no formal approval from the Royal
Society.

