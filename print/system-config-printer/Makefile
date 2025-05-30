PORTNAME=	system-config-printer
PORTVERSION=	1.5.12
PORTREVISION=	4
CATEGORIES=	print gnome

MAINTAINER=	gnome@FreeBSD.org
COMMENT=	CUPS configuration Gtk+2.0 GUI
WWW=		http://cyberelk.net/tim/software/system-config-printer/

BUILD_DEPENDS=	${PY_SETUPTOOLS} \
		xmlto:textproc/xmlto \
		docbook-xml>0:textproc/docbook-xml
LIB_DEPENDS=	libcups.so:print/cups
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}dbus>0:devel/py-dbus@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pycups>=0:print/py-pycups@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pycurl>=0:ftp/py-pycurl@${PY_FLAVOR} \
		${LOCALBASE}/libexec/cups-pk-helper-mechanism:print/cups-pk-helper

# 1.5 series is python3 ignore them for now.
PORTSCOUT=	limitw:1,even

GNU_CONFIGURE=	yes
GNU_CONFIGURE_MANPREFIX=${PREFIX}/share
USES=		autoreconf desktop-file-utils gettext gmake gnome pathfix \
		pkgconfig python shebangfix tar:xz

USE_GITHUB=	yes
GH_ACCOUNT=	OpenPrinting

CPPFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib
USE_GNOME=	intlhack pygobject3

CONFIGURE_ARGS=	--without-udev-rules \
		--without-systemdsystemunitdir
NO_ARCH=	yes

PLIST_SUB=	PYTHON_VER=${PYTHON_VERSION:S/python//}

SHEBANG_FILES=	*.py troubleshoot/*.py xml/validate.py

PYDISTUTILS_PKGNAME=	cupshelpers
PYDISTUTILS_PKGVERSION=	1.0

post-patch:
	@${REINPLACE_CMD} -e 's|%%LOCALBASE%%|${LOCALBASE}|g; \
		s|%%PREFIX%%|${PREFIX}|g' \
		${WRKSRC}/applet.py ${WRKSRC}/check-device-ids.py \
		${WRKSRC}/cupshelpers/cupshelpers.py \
		${WRKSRC}/cupshelpers/xmldriverprefs.py \
		${WRKSRC}/dbus/org.fedoraproject.Config.Printing.service.in \
		${WRKSRC}/newprinter.py ${WRKSRC}/probe_printer.py
	@${REINPLACE_CMD} -e 's|setup.py install.*|setup.py install -c -O1 --prefix=${PREFIX} --root=${STAGEDIR}|g' \
		${WRKSRC}/Makefile.am

.include <bsd.port.mk>
