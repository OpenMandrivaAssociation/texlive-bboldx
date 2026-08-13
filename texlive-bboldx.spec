%global tl_name bboldx
%global tl_revision 77682
%global tl_version 1.032

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Extension of the bbold package with a Blackboard Bold alphabet
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bboldx
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bboldx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bboldx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Extension of bbold to a package with three weights, of which the
original is considered as light and the additions as regular and bold.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from bboldx:
Map bboldx.map
TL_DROPIN_EOF
