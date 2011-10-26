BEGIN;
CREATE TABLE `blindado_device` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `client_id` integer NOT NULL,
    `active` bool NOT NULL,
    `accept` bool NOT NULL,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL
)
;
ALTER TABLE `blindado_device` ADD CONSTRAINT `client_id_refs_id_c48b6d50` FOREIGN KEY (`client_id`) REFERENCES `cliente_client` (`id`);
CREATE TABLE `blindado_ipdevice` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY,
    `alias` varchar(255) NOT NULL,
    `number_vulns_1` integer UNSIGNED NOT NULL,
    `number_vulns_2` integer UNSIGNED NOT NULL,
    `number_vulns_3` integer UNSIGNED NOT NULL,
    `number_vulns_4` integer UNSIGNED NOT NULL,
    `number_vulns_5` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `blindado_ipdevice` ADD CONSTRAINT `device_ptr_id_refs_id_e339f54c` FOREIGN KEY (`device_ptr_id`) REFERENCES `blindado_device` (`id`);
CREATE TABLE `blindado_urldevice` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY,
    `certified` bool NOT NULL,
    `description` longtext NOT NULL,
    `logo` varchar(100) NOT NULL,
    `number_access` integer UNSIGNED NOT NULL,
    `number_vulns_1` integer UNSIGNED NOT NULL,
    `number_vulns_2` integer UNSIGNED NOT NULL,
    `number_vulns_3` integer UNSIGNED NOT NULL,
    `number_vulns_4` integer UNSIGNED NOT NULL,
    `number_vulns_5` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `blindado_urldevice` ADD CONSTRAINT `device_ptr_id_refs_id_57c103b7` FOREIGN KEY (`device_ptr_id`) REFERENCES `blindado_device` (`id`);
CREATE TABLE `blindado_schedule` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `schedule_start` datetime NOT NULL,
    `schedule_finish` datetime NOT NULL,
    `scan_hour` time NOT NULL,
    `frequency` varchar(20) NOT NULL,
    `active` bool NOT NULL,
    `weekly_scan_day` integer UNSIGNED,
    `monthly_scan_day` integer UNSIGNED,
    `recurrent` bool NOT NULL,
    `created_by` integer,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL
)
;
CREATE TABLE `blindado_scantype` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(50) NOT NULL,
    `description` varchar(200) NOT NULL,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL
)
;
CREATE TABLE `blindado_scan` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `scan_date` datetime NOT NULL,
    `completed` bool NOT NULL,
    `schedule_id` integer NOT NULL,
    `scan_finished_date` datetime,
    `error_description` varchar(765) NOT NULL,
    `number_attempts` integer,
    `request_id` varchar(45) UNIQUE,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL
)
;
ALTER TABLE `blindado_scan` ADD CONSTRAINT `schedule_id_refs_id_f0636319` FOREIGN KEY (`schedule_id`) REFERENCES `blindado_schedule` (`id`);
CREATE TABLE `blindado_cenzicarmoredscan` (
    `scan_ptr_id` integer NOT NULL PRIMARY KEY,
    `status` varchar(20) NOT NULL,
    `percentage` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `blindado_cenzicarmoredscan` ADD CONSTRAINT `scan_ptr_id_refs_id_6ec5eef2` FOREIGN KEY (`scan_ptr_id`) REFERENCES `blindado_scan` (`id`);
CREATE TABLE `blindado_avdsarmoredscan` (
    `scan_ptr_id` integer NOT NULL PRIMARY KEY,
    `status` varchar(20) NOT NULL,
    `percentage` integer UNSIGNED NOT NULL,
    `scan_avds` varchar(100) NOT NULL,
    `webscan_avds_id` varchar(100) NOT NULL
)
;
ALTER TABLE `blindado_avdsarmoredscan` ADD CONSTRAINT `scan_ptr_id_refs_id_5505b172` FOREIGN KEY (`scan_ptr_id`) REFERENCES `blindado_scan` (`id`);
CREATE TABLE `blindado_qualysarmoredscan` (
    `scan_ptr_id` integer NOT NULL PRIMARY KEY,
    `status` varchar(20) NOT NULL,
    `percentage` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `blindado_qualysarmoredscan` ADD CONSTRAINT `scan_ptr_id_refs_id_9519e82b` FOREIGN KEY (`scan_ptr_id`) REFERENCES `blindado_scan` (`id`);
CREATE TABLE `blindado_armoredschedule` (
    `schedule_ptr_id` integer NOT NULL PRIMARY KEY,
    `device_id` integer NOT NULL,
    `scan_type_id` integer NOT NULL
)
;
ALTER TABLE `blindado_armoredschedule` ADD CONSTRAINT `schedule_ptr_id_refs_id_ff5153f4` FOREIGN KEY (`schedule_ptr_id`) REFERENCES `blindado_schedule` (`id`);
ALTER TABLE `blindado_armoredschedule` ADD CONSTRAINT `scan_type_id_refs_id_6f3b3920` FOREIGN KEY (`scan_type_id`) REFERENCES `blindado_scantype` (`id`);
ALTER TABLE `blindado_armoredschedule` ADD CONSTRAINT `device_id_refs_id_abdf218b` FOREIGN KEY (`device_id`) REFERENCES `blindado_device` (`id`);
CREATE TABLE `blindado_cenzicreport` (
    `report_ptr_id` integer NOT NULL PRIMARY KEY,
    `scan_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `blindado_cenzicreport` ADD CONSTRAINT `scan_id_refs_scan_ptr_id_5b0b132d` FOREIGN KEY (`scan_id`) REFERENCES `blindado_cenzicarmoredscan` (`scan_ptr_id`);
CREATE TABLE `blindado_avdsreport` (
    `report_ptr_id` integer NOT NULL PRIMARY KEY,
    `scan_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `blindado_avdsreport` ADD CONSTRAINT `scan_id_refs_scan_ptr_id_121fcf4b` FOREIGN KEY (`scan_id`) REFERENCES `blindado_avdsarmoredscan` (`scan_ptr_id`);
CREATE TABLE `blindado_qualysreport` (
    `report_ptr_id` integer NOT NULL PRIMARY KEY,
    `scan_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `blindado_qualysreport` ADD CONSTRAINT `scan_id_refs_scan_ptr_id_7496a7fd` FOREIGN KEY (`scan_id`) REFERENCES `blindado_qualysarmoredscan` (`scan_ptr_id`);
-- The following references should be added but depend on non-existent tables:
-- ALTER TABLE `blindado_cenzicreport` ADD CONSTRAINT `report_ptr_id_refs_id_afadac6a` FOREIGN KEY (`report_ptr_id`) REFERENCES `models_report` (`id`);
-- ALTER TABLE `blindado_avdsreport` ADD CONSTRAINT `report_ptr_id_refs_id_5566bf72` FOREIGN KEY (`report_ptr_id`) REFERENCES `models_report` (`id`);
-- ALTER TABLE `blindado_qualysreport` ADD CONSTRAINT `report_ptr_id_refs_id_e040f31b` FOREIGN KEY (`report_ptr_id`) REFERENCES `models_report` (`id`);
CREATE INDEX `blindado_device_4a4e8ffb` ON `blindado_device` (`client_id`);
CREATE INDEX `blindado_scan_10d3e039` ON `blindado_scan` (`schedule_id`);
CREATE INDEX `blindado_armoredschedule_5b7abc50` ON `blindado_armoredschedule` (`device_id`);
CREATE INDEX `blindado_armoredschedule_172d13d7` ON `blindado_armoredschedule` (`scan_type_id`);
CREATE TABLE `malware_malwaredevice` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY,
    `alias` varchar(255) NOT NULL,
    `certified` bool NOT NULL,
    `number_links` integer UNSIGNED NOT NULL,
    `number_links_additional` integer UNSIGNED NOT NULL,
    `removed` bool NOT NULL,
    `blocked_trial` bool NOT NULL,
    `release_seal` bool NOT NULL
)
;
ALTER TABLE `malware_malwaredevice` ADD CONSTRAINT `device_ptr_id_refs_id_4dd79a72` FOREIGN KEY (`device_ptr_id`) REFERENCES `blindado_device` (`id`);
CREATE TABLE `malware_malwareschedule` (
    `schedule_ptr_id` integer NOT NULL PRIMARY KEY,
    `device_id` integer NOT NULL
)
;
ALTER TABLE `malware_malwareschedule` ADD CONSTRAINT `device_id_refs_device_ptr_id_34ed0b2c` FOREIGN KEY (`device_id`) REFERENCES `malware_malwaredevice` (`device_ptr_id`);
-- The following references should be added but depend on non-existent tables:
-- ALTER TABLE `malware_malwareschedule` ADD CONSTRAINT `schedule_ptr_id_refs_id_105dcb78` FOREIGN KEY (`schedule_ptr_id`) REFERENCES `blindado_schedule` (`id`);
CREATE INDEX `malware_malwareschedule_5b7abc50` ON `malware_malwareschedule` (`device_id`);
CREATE TABLE `cliente_client` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `cep` varchar(9) NOT NULL,
    `address` varchar(255) NOT NULL,
    `complement` varchar(255) NOT NULL,
    `neighborhood` varchar(255) NOT NULL,
    `city` varchar(100) NOT NULL,
    `province` varchar(2) NOT NULL,
    `phone` varchar(20) NOT NULL,
    `fax` varchar(20) NOT NULL,
    `cellphone` varchar(20) NOT NULL,
    `active` bool NOT NULL,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL,
    `logo` varchar(100) NOT NULL,
    `activation_code` varchar(100) NOT NULL,
    `activated_at` datetime NOT NULL,
    `level` integer UNSIGNED NOT NULL,
    `scan_provider_url` integer UNSIGNED NOT NULL,
    `scan_provider_ip` integer UNSIGNED NOT NULL,
    `online` bool NOT NULL,
    `number` integer UNSIGNED NOT NULL,
    `owner` bool NOT NULL,
    `cep_return` integer UNSIGNED NOT NULL,
    `sid` varchar(100) NOT NULL,
    `vip_client` bool NOT NULL
)
;
CREATE TABLE `cliente_individual` (
    `client_ptr_id` integer NOT NULL PRIMARY KEY,
    `email` varchar(75) NOT NULL,
    `cpf` integer UNSIGNED NOT NULL,
    `rg` varchar(15) NOT NULL
)
;
ALTER TABLE `cliente_individual` ADD CONSTRAINT `client_ptr_id_refs_id_e0adbc6d` FOREIGN KEY (`client_ptr_id`) REFERENCES `cliente_client` (`id`);
CREATE TABLE `cliente_legalentity` (
    `client_ptr_id` integer NOT NULL PRIMARY KEY,
    `cnpj` integer UNSIGNED NOT NULL,
    `state_registration` varchar(100) NOT NULL,
    `name_representant` varchar(255) NOT NULL,
    `email_representant` varchar(75) NOT NULL,
    `rg_representant` varchar(255) NOT NULL,
    `cpf_representant` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `cliente_legalentity` ADD CONSTRAINT `client_ptr_id_refs_id_dadab249` FOREIGN KEY (`client_ptr_id`) REFERENCES `cliente_client` (`id`);
CREATE TABLE `cliente_acquirer` (
    `client_ptr_id` integer NOT NULL PRIMARY KEY,
    `max_num_ips_pci` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `cliente_acquirer` ADD CONSTRAINT `client_ptr_id_refs_id_11cf076` FOREIGN KEY (`client_ptr_id`) REFERENCES `cliente_client` (`id`);
COMMIT;
