%global packname  BSgenome.Celegans.UCSC.ce2
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.3.19
Release:          1
Summary:          Caenorhabditis elegans (Worm) full genome (UCSC version ce2)
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              https://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Celegans.UCSC.ce2_1.3.19.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-BSgenome 
Requires:         R-BSgenome 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-BSgenome
BuildRequires:    R-BSgenome 

%description
Caenorhabditis elegans (Worm) full genome as provided by UCSC (ce2, Mar.
2004) and stored in Biostrings objects.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help

