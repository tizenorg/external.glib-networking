/* GIO - GLib Input, Output and Streaming Library
 *
 * Copyright 2010 Collabora, Ltd.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published
 * by the Free Software Foundation; either version 2 of the licence or (at
 * your option) any later version.
 *
 * See the included COPYING file for more information.
 *
 * Author: Stef Walter <stefw@collabora.co.uk>
 */

#ifndef __G_TLS_FILE_DATABASE_GNUTLS_H__
#define __G_TLS_FILE_DATABASE_GNUTLS_H__

#include <gio/gio.h>

#include "gtlsdatabase-gnutls.h"

G_BEGIN_DECLS

#define G_TYPE_TLS_FILE_DATABASE_GNUTLS            (g_tls_file_database_gnutls_get_type ())
#define G_TLS_FILE_DATABASE_GNUTLS(inst)           (G_TYPE_CHECK_INSTANCE_CAST ((inst), G_TYPE_TLS_FILE_DATABASE_GNUTLS, GTlsFileDatabaseGnutls))
#define G_TLS_FILE_DATABASE_GNUTLS_CLASS(class)    (G_TYPE_CHECK_CLASS_CAST ((class), G_TYPE_TLS_FILE_DATABASE_GNUTLS, GTlsFileDatabaseGnutlsClass))
#define G_IS_TLS_FILE_DATABASE_GNUTLS(inst)        (G_TYPE_CHECK_INSTANCE_TYPE ((inst), G_TYPE_TLS_FILE_DATABASE_GNUTLS))
#define G_IS_TLS_FILE_DATABASE_GNUTLS_CLASS(class) (G_TYPE_CHECK_CLASS_TYPE ((class), G_TYPE_TLS_FILE_DATABASE_GNUTLS))
#define G_TLS_FILE_DATABASE_GNUTLS_GET_CLASS(inst) (G_TYPE_INSTANCE_GET_CLASS ((inst), G_TYPE_TLS_FILE_DATABASE_GNUTLS, GTlsFileDatabaseGnutlsClass))

typedef struct _GTlsFileDatabaseGnutlsPrivate                   GTlsFileDatabaseGnutlsPrivate;
typedef struct _GTlsFileDatabaseGnutlsClass                     GTlsFileDatabaseGnutlsClass;
typedef struct _GTlsFileDatabaseGnutls                          GTlsFileDatabaseGnutls;

struct _GTlsFileDatabaseGnutlsClass
{
  GTlsDatabaseGnutlsClass parent_class;
};

struct _GTlsFileDatabaseGnutls
{
  GTlsDatabaseGnutls parent_instance;
  GTlsFileDatabaseGnutlsPrivate *priv;
};

GType                        g_tls_file_database_gnutls_get_type              (void) G_GNUC_CONST;

GTlsDatabase*                g_tls_file_database_gnutls_new                   (const gchar *anchor_file);

G_END_DECLS

#endif /* __G_TLS_FILE_DATABASE_GNUTLS_H___ */
