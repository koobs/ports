PKGNAMESUFFIX=	${PHP_PKGNAMESUFFIX}

UNIT_MODNAME=	php${PHP_VER}

COMMENT=	PHP module for NGINX Unit

PLIST_FILES=	libexec/unit/modules/${UNIT_MODNAME}.unit.so

RUN_DEPENDS=	unitd:www/unit

USES=		php:build,embed,flavors

USE_RC_SUBR=	# reset to empty

MASTERDIR=	${.CURDIR}/../unit

post-configure:
	cd ${CONFIGURE_WRKSRC} && \
	${SETENV} ${CONFIGURE_ENV} ${CONFIGURE_CMD} php \
		--lib-path=${LOCALBASE}/lib \
		--module=${UNIT_MODNAME}

do-build:
	cd ${CONFIGURE_WRKSRC} && \
	${SETENV} ${MAKE_ENV} ${MAKE_CMD} ${MAKE_FLAGS} \
		${MAKEFILE} ${MAKE_ARGS} ${UNIT_MODNAME}

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/libexec/unit/modules/
	${INSTALL_LIB} ${WRKSRC}/build/lib/unit/modules/${UNIT_MODNAME}.unit.so \
		${STAGEDIR}${PREFIX}/libexec/unit/modules/

.include "${MASTERDIR}/Makefile"
