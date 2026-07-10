%global tl_name bboldx
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.032
Release:	%{tl_revision}.1
Summary:	Extension of the bbold package with a Blackboard Bold alphabet
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bboldx
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bboldx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bboldx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Extension of bbold to a package with three weights, of which the
original is considered as light and the additions as regular and bold.

