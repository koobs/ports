PORTNAME=	dropbear
PORTVERSION=	2025.88
CATEGORIES=	security
MASTER_SITES=	https://matt.ucc.asn.au/dropbear/releases/

MAINTAINER=	pkubaj@FreeBSD.org
COMMENT=	SSH 2 server, designed to be usable in small memory environments
WWW=		https://matt.ucc.asn.au/dropbear/dropbear.html

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		cpe gmake tar:bzip2
CPE_VENDOR=	dropbear_ssh_project
CPE_PRODUCT=	dropbear_ssh

GNU_CONFIGURE=	yes
USE_RC_SUBR=	${PORTNAME}
ALL_TARGET=	all scp

OPTIONS_DEFINE=		SMALL_CODE PORTS_LIBTOM STATIC X11FWD
OPTIONS_DEFAULT=	AES128 AES256 CURVE25519 ECDSA ED25519 GCM \
			GROUP14_SHA256 GROUP16 PORTS_LIBTOM RSA SHA2_256 \
			MLKEM768 SNTRUP761
OPTIONS_MULTI=		ENC KEY KEX MAC MODE
OPTIONS_MULTI_ENC=	3DES AES128 AES256 CHACHA20POLY1305
OPTIONS_MULTI_KEY=	DSS ECDSA ED25519 RSA
OPTIONS_MULTI_KEX=	CURVE25519 ECDH GROUP1 GROUP14_SHA1 GROUP14_SHA256 \
			GROUP16 MLKEM768 SNTRUP761
OPTIONS_MULTI_MAC=	MD5 RSA_SHA1 SHA1 SHA1_96 SHA2_256 SHA2_512
OPTIONS_MULTI_MODE=	CBC CTR GCM

3DES_DESC=		Enable 3DES-based encryption
AES128_DESC=		Enable AES128-based encryption
AES256_DESC=		Enable AES256-based encryption
CBC_DESC=		Use CBC mode for ciphers (less secure)
CHACHA20POLY1305_DESC=	Enable chacha20poly1305-based encryption
CTR_DESC=		Use CTR mode for ciphers
CURVE25519_DESC=	Enable Curve25519
DSS_DESC=		Enable DSS (insecure)
ECDH_DESC=		Enable ECDH (insecure)
ECDSA_DESC=		Enable ECDSA public key support
ED25519_DESC=		Enable ED25519 public key support
GCM_DESC=		Enable GCM mode for ciphers (more secure)
GROUP14_SHA1_DESC=	Enable Group14 Diffie-Helman with SHA1 (insecure)
GROUP14_SHA256_DESC=	Enable Group14 Diffie-Helman with SHA256
GROUP16_DESC=		Enable Group16 Diffie-Hellman
GROUP1_DESC=		Enable Group1 Diffie-Hellman (insecure)
MD5_DESC=		Enable MD5 MAC (broken)
MLKEM768_DESC=		Enable mlkem768 key exchange algorithm (recommended)
SNTRUP761_DESC=		Enable sntrup761 key exchange algorithm (recommended)
PORTS_LIBTOM_DESC=	Use libtomcrypt/libtommath in ports tree
RSA_DESC=		Enable RSA public key support
RSA_SHA1_DESC=		Enable RSA SHA1 MAC (insecure)
SHA1_96_DESC=		Enable SHA1_96 MAC (less secure)
SHA1_DESC=		Enable SHA1 MAC (less secure)
SHA2_256_DESC=		Enable SHA2_256 MAC
SHA2_512_DESC=		Enable SHA2_512 MAC
SMALL_CODE_DESC=	Make binary smaller in exchange for 50% performance hit
X11FWD_DESC=		Enable X11 forwarding

3DES_IMPLIES=	CTR
CBC_IMPLIES=	CTR

PORTS_LIBTOM_USES=		localbase:ldflags
PORTS_LIBTOM_CONFIGURE_ON=	--disable-bundled-libtom
PORTS_LIBTOM_CONFIGURE_OFF=	--enable-bundled-libtom

STATIC_CONFIGURE_ENABLE=	static

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MPORTS_LIBTOM} && ${PORT_OPTIONS:MSTATIC}
BUILD_DEPENDS=	${LOCALBASE}/lib/libtomcrypt.a:security/libtomcrypt \
		${LOCALBASE}/lib/libtommath.a:math/libtommath
.endif

.if ${PORT_OPTIONS:MPORTS_LIBTOM} && !${PORT_OPTIONS:MSTATIC}
LIB_DEPENDS=	libtomcrypt.so:security/libtomcrypt \
		libtommath.so:math/libtommath
.endif

post-patch:
	@${REINPLACE_CMD} -e "s,_PRIV_FILENAME \"/etc/,_PRIV_FILENAME \"${PREFIX}/etc/,g; \
		s,/usr/bin/X11/,${LOCALBASE}/,g" ${WRKSRC}/src/default_options.h

post-patch-SMALL_CODE-off:
	@${ECHO} "#define DROPBEAR_SMALL_CODE 0" >> ${WRKSRC}/localoptions.h

post-patch-3DES-on:
	@${ECHO} "#define DROPBEAR_3DES 1" >> ${WRKSRC}/localoptions.h

post-patch-AES128-off:
	@${ECHO} "#define DROPBEAR_AES128 0" >> ${WRKSRC}/localoptions.h

post-patch-AES256-off:
	@${ECHO} "#define DROPBEAR_AES256 0" >> ${WRKSRC}/localoptions.h

post-patch-CHACHA20POLY1305-off:
	@${ECHO} "#define DROPBEAR_CHACHA20POLY1305 0" >> ${WRKSRC}/localoptions.h

post-patch-CBC-on:
	@${ECHO} "#define DROPBEAR_ENABLE_CBC_MODE 1" >> ${WRKSRC}/localoptions.h

post-patch-CTR-off:
	@${ECHO} "#define DROPBEAR_ENABLE_CTR_MODE 0" >> ${WRKSRC}/localoptions.h

post-patch-GCM-on:
	@${ECHO} "#define DROPBEAR_ENABLE_GCM_MODE 1" >> ${WRKSRC}/localoptions.h

post-patch-CURVE25519-off:
	@${ECHO} "#define DROPBEAR_CURVE25519 0" >> ${WRKSRC}/localoptions.h

post-patch-DSS-on:
	@${ECHO} "#define DROPBEAR_DSS 1" >> ${WRKSRC}/localoptions.h

post-patch-ECDH-off:
	@${ECHO} "#define DROPBEAR_ECDH 0" >> ${WRKSRC}/localoptions.h

post-patch-GROUP1-off:
	@${ECHO} "#define DROPBEAR_DH_GROUP1 0" >> ${WRKSRC}/localoptions.h

post-patch-GROUP14_SHA1-off:
	@${ECHO} "#define DROPBEAR_DH_GROUP14_SHA1 0" >> ${WRKSRC}/localoptions.h

post-patch-GROUP14_SHA256-off:
	@${ECHO} "#define DROPBEAR_DH_GROUP14_SHA256 0" >> ${WRKSRC}/localoptions.h

post-patch-GROUP16-on:
	@${ECHO} "#define DROPBEAR_DH_GROUP16 1" >> ${WRKSRC}/localoptions.h

post-patch-RSA-off:
	@${ECHO} "#define DROPBEAR_RSA 0" >> ${WRKSRC}/localoptions.h

post-patch-RSA_SHA1-off:
	@${ECHO} "#define DROPBEAR_RSA_SHA1 0" >> ${WRKSRC}/localoptions.h

post-patch-ECDSA-off:
	@${ECHO} "#define DROPBEAR_ECDSA 0" >> ${WRKSRC}/localoptions.h

post-patch-ED25519-off:
	@${ECHO} "#define DROPBEAR_E25519 0" >> ${WRKSRC}/localoptions.h

post-patch-MD5-on:
	@${ECHO} "#define DROPBEAR_MD5_HMAC 1" >> ${WRKSRC}/localoptions.h

post-patch-MLKEM768-off:
	@${ECHO} "#define DROPBEAR_MLKEM768 0" >> ${WRKSRC}/localoptions.h

post-patch-SHA1-off:
	@${ECHO} "#define DROPBEAR_SHA1_HMAC 0" >> ${WRKSRC}/localoptions.h

post-patch-SHA1_96-off:
	@${ECHO} "#define DROPBEAR_SHA1_96_HMAC 0" >> ${WRKSRC}/localoptions.h

post-patch-SHA2_256-off:
	@${ECHO} "#define DROPBEAR_SHA2_256_HMAC 0" >> ${WRKSRC}/localoptions.h

post-patch-SHA2_512-on:
	@${ECHO} "#define DROPBEAR_SHA2_512_HMAC 1" >> ${WRKSRC}/localoptions.h

post-patch-SNTRUP761-off:
	@${ECHO} "#define DROPBEAR_SNTRUP761 0" >> ${WRKSRC}/localoptions.h

post-patch-X11FWD-on:
	@${ECHO} "#define DROPBEAR_X11FWD 1" >> ${WRKSRC}/localoptions.h

post-install:
	@${MKDIR} ${STAGEDIR}${PREFIX}/etc/dropbear
	${INSTALL_PROGRAM} ${WRKSRC}/scp ${STAGEDIR}${PREFIX}/bin/dbscp
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/dropbearconvert
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/dropbearkey
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/dbclient
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/sbin/dropbear

.include <bsd.port.mk>
