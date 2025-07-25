default_roles = {
    "Owner": {
        "meta": {
            "version": 2,
            "description": "The organisation owner, limited to a single user, with full access to all resources and actions.",
        },
        "permissions": {
            "Organisation": ["create", "read", "update", "delete"],
            "Billing": ["create", "read", "update", "delete"],
            "Apps": ["create", "read", "update", "delete"],
            "Members": ["create", "read", "update", "delete"],
            "MemberPersonalAccessTokens": ["create", "read", "update", "delete"],
            "ServiceAccounts": ["create", "read", "update", "delete"],
            "ServiceAccountTokens": ["create", "read", "update", "delete"],
            "Roles": ["create", "read", "update", "delete"],
            "IntegrationCredentials": ["create", "read", "update", "delete"],
            "NetworkAccessPolicies": ["create", "read", "update", "delete"],
        },
        "app_permissions": {
            "Environments": ["create", "read", "update", "delete"],
            "Secrets": ["create", "read", "update", "delete"],
            "Lockbox": ["create", "read", "update", "delete"],
            "Logs": ["create", "read", "update", "delete"],
            "Tokens": ["create", "read", "update", "delete"],
            "Members": ["create", "read", "update", "delete"],
            "ServiceAccounts": ["create", "read", "update", "delete"],
            "Integrations": ["create", "read", "update", "delete"],
            "EncryptionMode": ["read", "update"],
        },
        "global_access": True,
    },
    "Admin": {
        "meta": {
            "version": 2,
            "description": "Administrative users with broad access to resources and global access to all Apps and Environments.",
        },
        "permissions": {
            "Organisation": ["read", "update"],
            "Billing": ["create", "read", "update", "delete"],
            "Apps": ["create", "read", "update", "delete"],
            "Members": ["create", "read", "update", "delete"],
            "MemberPersonalAccessTokens": ["create", "read", "update", "delete"],
            "ServiceAccounts": ["create", "read", "update", "delete"],
            "ServiceAccountTokens": ["create", "read", "update", "delete"],
            "Roles": ["create", "read", "update", "delete"],
            "IntegrationCredentials": ["create", "read", "update", "delete"],
            "NetworkAccessPolicies": ["create", "read", "update", "delete"],
        },
        "app_permissions": {
            "Environments": ["create", "read", "update", "delete"],
            "Secrets": ["create", "read", "update", "delete"],
            "Lockbox": ["create", "read", "update", "delete"],
            "Logs": ["create", "read", "update", "delete"],
            "Tokens": ["create", "read", "update", "delete"],
            "Members": ["create", "read", "update", "delete"],
            "ServiceAccounts": ["create", "read", "update", "delete"],
            "Integrations": ["create", "read", "update", "delete"],
            "EncryptionMode": ["read", "update"],
        },
        "global_access": True,
    },
    "Manager": {
        "meta": {
            "version": 2,
            "description": "Management users with broad access to environments, secrets, and service accounts at the organisation level. Requires explicit access to Apps and Environments.",
        },
        "permissions": {
            "Organisation": ["read"],
            "Billing": ["create", "read", "update", "delete"],
            "Apps": ["create", "read", "update", "delete"],
            "Members": ["create", "read", "update", "delete"],
            "ServiceAccounts": ["create", "read", "update", "delete"],
            "ServiceAccountTokens": ["create", "read", "update", "delete"],
            "Roles": ["create", "read", "update", "delete"],
            "IntegrationCredentials": ["create", "read", "update", "delete"],
            "NetworkAccessPolicies": ["create", "read", "update", "delete"],
        },
        "app_permissions": {
            "Environments": ["read", "create", "update"],
            "Secrets": ["create", "read", "update", "delete"],
            "Lockbox": ["create", "read", "update", "delete"],
            "Logs": ["create", "read", "update", "delete"],
            "Tokens": ["create", "read", "update", "delete"],
            "Members": ["create", "read", "update", "delete"],
            "ServiceAccounts": ["create", "read", "update", "delete"],
            "Integrations": ["create", "read", "update", "delete"],
            "EncryptionMode": ["read", "update"],
        },
        "global_access": False,
    },
    "Developer": {
        "meta": {
            "version": 1,
            "description": "Development users with limited organisation-level permissions. Requires explicit access to Apps and Environments.",
        },
        "permissions": {
            "Organisation": [],
            "Billing": [],
            "Apps": ["read"],
            "Members": ["read"],
            "ServiceAccounts": [],
            "ServiceAccountTokens": [],
            "Roles": ["read"],
            "IntegrationCredentials": [
                "create",
                "read",
                "update",
            ],
            "NetworkAccessPolicies": ["read"],
        },
        "app_permissions": {
            "Environments": ["read", "create", "update"],
            "Secrets": ["create", "read", "update", "delete"],
            "Lockbox": ["create", "read", "update", "delete"],
            "Logs": ["read"],
            "Tokens": ["read", "create"],
            "Members": ["read"],
            "ServiceAccounts": ["create"],
            "Integrations": ["create", "read", "update", "delete"],
            "EncryptionMode": ["read", "update"],
        },
        "global_access": False,
    },
    "Service": {
        "meta": {
            "version": 1,
            "description": "Default role for Service Accounts, providing programmatic access to secrets without access to other organisation or app resources.",
        },
        "permissions": {
            "Organisation": [],
            "Billing": [],
            "Apps": ["create", "read", "update"],
            "Members": ["read"],
            "ServiceAccounts": ["read"],
            "ServiceAccountTokens": ["read"],
            "Roles": ["read"],
            "IntegrationCredentials": ["read"],
            "NetworkAccessPolicies": ["read"],
        },
        "app_permissions": {
            "Environments": ["read", "create", "update", "delete"],
            "Secrets": ["create", "read", "update", "delete"],
            "Lockbox": [],
            "Logs": [],
            "Tokens": [],
            "Members": ["read"],
            "ServiceAccounts": ["read"],
            "Integrations": ["read"],
            "EncryptionMode": ["read"],
        },
        "global_access": False,
    },
}
