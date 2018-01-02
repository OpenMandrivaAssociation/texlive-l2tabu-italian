Name:		texlive-l2tabu-italian
Version:	2.3
Release:	1
Summary:	Italian Translation of Obsolete packages and commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2tabu/italian
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-italian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2tabu-italian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Italian translation of the l2tabu practical guide to LaTeX2e (a
list of obsolete packages and commands).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/l2tabu-italian

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
