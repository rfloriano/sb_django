BEGIN;
CREATE TABLE `core_client` (
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
CREATE TABLE `core_individual` (
    `client_ptr_id` integer NOT NULL PRIMARY KEY,
    `email` varchar(75) NOT NULL,
    `cpf` integer UNSIGNED NOT NULL,
    `rg` varchar(15) NOT NULL
)
;
ALTER TABLE `core_individual` ADD CONSTRAINT `client_ptr_id_refs_id_83f65b61` FOREIGN KEY (`client_ptr_id`) REFERENCES `core_client` (`id`);
CREATE TABLE `core_legalentity` (
    `client_ptr_id` integer NOT NULL PRIMARY KEY,
    `cnpj` integer UNSIGNED NOT NULL,
    `state_registration` varchar(100) NOT NULL,
    `name_representant` varchar(255) NOT NULL,
    `email_representant` varchar(75) NOT NULL,
    `rg_representant` varchar(255) NOT NULL,
    `cpf_representant` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `core_legalentity` ADD CONSTRAINT `client_ptr_id_refs_id_a79a8c5b` FOREIGN KEY (`client_ptr_id`) REFERENCES `core_client` (`id`);
CREATE TABLE `core_acquirer` (
    `client_ptr_id` integer NOT NULL PRIMARY KEY,
    `max_num_ips_pci` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `core_acquirer` ADD CONSTRAINT `client_ptr_id_refs_id_54ef626a` FOREIGN KEY (`client_ptr_id`) REFERENCES `core_client` (`id`);
CREATE TABLE `core_device` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `client_id` integer NOT NULL,
    `active` bool NOT NULL,
    `accept` bool NOT NULL,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL
)
;
ALTER TABLE `core_device` ADD CONSTRAINT `client_id_refs_id_1c6f20d0` FOREIGN KEY (`client_id`) REFERENCES `core_client` (`id`);
CREATE TABLE `core_contract` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `client_id` integer NOT NULL,
    `start_date` date NOT NULL,
    `end_date` date NOT NULL,
    `cancel_date` date,
    `active` bool NOT NULL,
    `trial` bool NOT NULL,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL
)
;
ALTER TABLE `core_contract` ADD CONSTRAINT `client_id_refs_id_9ff4d2ba` FOREIGN KEY (`client_id`) REFERENCES `core_client` (`id`);
CREATE TABLE `core_plan` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(150) NOT NULL,
    `description` longtext NOT NULL,
    `frequency` varchar(100) NOT NULL,
    `time_trial` integer UNSIGNED NOT NULL,
    `seal` bool NOT NULL,
    `use_akamai` bool NOT NULL,
    `page_view_limit` bool NOT NULL,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL
)
;
CREATE TABLE `core_planrange` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `plan_id` integer NOT NULL,
    `description` longtext NOT NULL,
    `price` numeric(10, 2) NOT NULL,
    `price_anual` numeric(10, 2) NOT NULL,
    `start_price` numeric(10, 2) NOT NULL,
    `dialy_page_views` integer UNSIGNED NOT NULL,
    `monthly_page_views` integer UNSIGNED NOT NULL,
    `finance_code` integer NOT NULL,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL
)
;
ALTER TABLE `core_planrange` ADD CONSTRAINT `plan_id_refs_id_954667e5` FOREIGN KEY (`plan_id`) REFERENCES `core_plan` (`id`);
CREATE TABLE `core_plancontract` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `contract_id` integer NOT NULL,
    `plan_id` integer NOT NULL,
    `plan_price` numeric(10, 2) NOT NULL,
    `aditional_link_price` numeric(10, 2) NOT NULL,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL
)
;
ALTER TABLE `core_plancontract` ADD CONSTRAINT `contract_id_refs_id_309baae0` FOREIGN KEY (`contract_id`) REFERENCES `core_contract` (`id`);
ALTER TABLE `core_plancontract` ADD CONSTRAINT `plan_id_refs_id_528e788d` FOREIGN KEY (`plan_id`) REFERENCES `core_plan` (`id`);
CREATE TABLE `core_vulnerability` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `title` varchar(255) NOT NULL,
    `vuln_type` varchar(255) NOT NULL,
    `severity_level` integer UNSIGNED NOT NULL,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL
)
;
CREATE TABLE `core_reference` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `url_reference` varchar(200) NOT NULL,
    `vulnerability_id` integer NOT NULL,
    `vulnerability_type` varchar(150) NOT NULL
)
;
ALTER TABLE `core_reference` ADD CONSTRAINT `vulnerability_id_refs_id_7730d8de` FOREIGN KEY (`vulnerability_id`) REFERENCES `core_vulnerability` (`id`);
CREATE TABLE `core_schedule` (
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
CREATE TABLE `core_scantype` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(50) NOT NULL,
    `description` varchar(200) NOT NULL,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL
)
;
CREATE TABLE `core_scan` (
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
ALTER TABLE `core_scan` ADD CONSTRAINT `schedule_id_refs_id_36cf7781` FOREIGN KEY (`schedule_id`) REFERENCES `core_schedule` (`id`);
CREATE INDEX `core_device_4a4e8ffb` ON `core_device` (`client_id`);
CREATE INDEX `core_contract_4a4e8ffb` ON `core_contract` (`client_id`);
CREATE INDEX `core_planrange_a57fd7f1` ON `core_planrange` (`plan_id`);
CREATE INDEX `core_plancontract_b07bb6ae` ON `core_plancontract` (`contract_id`);
CREATE INDEX `core_plancontract_a57fd7f1` ON `core_plancontract` (`plan_id`);
CREATE INDEX `core_reference_43a42eb3` ON `core_reference` (`vulnerability_id`);
CREATE INDEX `core_scan_10d3e039` ON `core_scan` (`schedule_id`);
CREATE TABLE `armored_report` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created_at` datetime NOT NULL,
    `updated_at` datetime NOT NULL
)
;
CREATE TABLE `armored_reportvulnerability` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `report_id` integer NOT NULL,
    `vulnerability_id` integer NOT NULL,
    `reference_id` integer NOT NULL
)
;
ALTER TABLE `armored_reportvulnerability` ADD CONSTRAINT `vulnerability_id_refs_id_cbde8827` FOREIGN KEY (`vulnerability_id`) REFERENCES `core_vulnerability` (`id`);
ALTER TABLE `armored_reportvulnerability` ADD CONSTRAINT `report_id_refs_id_8cb9d0c8` FOREIGN KEY (`report_id`) REFERENCES `armored_report` (`id`);
ALTER TABLE `armored_reportvulnerability` ADD CONSTRAINT `reference_id_refs_id_707f40` FOREIGN KEY (`reference_id`) REFERENCES `core_reference` (`id`);
CREATE TABLE `armored_armoredplanrange` (
    `planrange_ptr_id` integer NOT NULL PRIMARY KEY,
    `ips_quantity` integer UNSIGNED NOT NULL,
    `urls_quantity` integer UNSIGNED NOT NULL,
    `pci_quantity` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `armored_armoredplanrange` ADD CONSTRAINT `planrange_ptr_id_refs_id_3151466e` FOREIGN KEY (`planrange_ptr_id`) REFERENCES `core_planrange` (`id`);
CREATE TABLE `armored_armoredplancontract` (
    `plancontract_ptr_id` integer NOT NULL PRIMARY KEY,
    `device_id` integer NOT NULL
)
;
ALTER TABLE `armored_armoredplancontract` ADD CONSTRAINT `device_id_refs_id_5bf4d6a9` FOREIGN KEY (`device_id`) REFERENCES `core_device` (`id`);
ALTER TABLE `armored_armoredplancontract` ADD CONSTRAINT `plancontract_ptr_id_refs_id_2928c77c` FOREIGN KEY (`plancontract_ptr_id`) REFERENCES `core_plancontract` (`id`);
CREATE TABLE `armored_ipdevice` (
    `device_ptr_id` integer NOT NULL PRIMARY KEY,
    `alias` varchar(255) NOT NULL,
    `number_vulns_1` integer UNSIGNED NOT NULL,
    `number_vulns_2` integer UNSIGNED NOT NULL,
    `number_vulns_3` integer UNSIGNED NOT NULL,
    `number_vulns_4` integer UNSIGNED NOT NULL,
    `number_vulns_5` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `armored_ipdevice` ADD CONSTRAINT `device_ptr_id_refs_id_d91d4850` FOREIGN KEY (`device_ptr_id`) REFERENCES `core_device` (`id`);
CREATE TABLE `armored_urldevice` (
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
ALTER TABLE `armored_urldevice` ADD CONSTRAINT `device_ptr_id_refs_id_ada7ff0f` FOREIGN KEY (`device_ptr_id`) REFERENCES `core_device` (`id`);
CREATE TABLE `armored_avdsarmoredscan` (
    `scan_ptr_id` integer NOT NULL PRIMARY KEY,
    `status` varchar(20) NOT NULL,
    `percentage` integer UNSIGNED NOT NULL,
    `scan_avds` varchar(100) NOT NULL,
    `webscan_avds_id` varchar(100) NOT NULL
)
;
ALTER TABLE `armored_avdsarmoredscan` ADD CONSTRAINT `scan_ptr_id_refs_id_afaf3ed2` FOREIGN KEY (`scan_ptr_id`) REFERENCES `core_scan` (`id`);
CREATE TABLE `armored_avdsreport` (
    `report_ptr_id` integer NOT NULL PRIMARY KEY,
    `scan_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `armored_avdsreport` ADD CONSTRAINT `report_ptr_id_refs_id_790a4f9b` FOREIGN KEY (`report_ptr_id`) REFERENCES `armored_report` (`id`);
ALTER TABLE `armored_avdsreport` ADD CONSTRAINT `scan_id_refs_scan_ptr_id_5a800819` FOREIGN KEY (`scan_id`) REFERENCES `armored_avdsarmoredscan` (`scan_ptr_id`);
CREATE TABLE `armored_avdsvulnerability` (
    `vulnerability_ptr_id` integer NOT NULL PRIMARY KEY,
    `provider_id` integer NOT NULL UNIQUE,
    `family` longtext NOT NULL,
    `name` longtext NOT NULL,
    `description` longtext NOT NULL,
    `how_it_works` longtext NOT NULL,
    `impact` longtext NOT NULL,
    `solution` longtext NOT NULL,
    `risk` integer,
    `test_id` integer,
    `service` varchar(255) NOT NULL
)
;
ALTER TABLE `armored_avdsvulnerability` ADD CONSTRAINT `vulnerability_ptr_id_refs_id_c2204a6d` FOREIGN KEY (`vulnerability_ptr_id`) REFERENCES `core_vulnerability` (`id`);
CREATE TABLE `armored_avdsreference` (
    `reference_ptr_id` integer NOT NULL PRIMARY KEY,
    `mensagem` longtext NOT NULL,
    `data_criacao` datetime,
    `http_request` longtext NOT NULL,
    `http_response` longtext NOT NULL
)
;
ALTER TABLE `armored_avdsreference` ADD CONSTRAINT `reference_ptr_id_refs_id_75d8bf53` FOREIGN KEY (`reference_ptr_id`) REFERENCES `core_reference` (`id`);
CREATE TABLE `armored_cenzicarmoredscan` (
    `scan_ptr_id` integer NOT NULL PRIMARY KEY,
    `status` varchar(20) NOT NULL,
    `percentage` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `armored_cenzicarmoredscan` ADD CONSTRAINT `scan_ptr_id_refs_id_e76a1ad2` FOREIGN KEY (`scan_ptr_id`) REFERENCES `core_scan` (`id`);
CREATE TABLE `armored_cenzicreport` (
    `report_ptr_id` integer NOT NULL PRIMARY KEY,
    `scan_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `armored_cenzicreport` ADD CONSTRAINT `scan_id_refs_scan_ptr_id_c3811c67` FOREIGN KEY (`scan_id`) REFERENCES `armored_cenzicarmoredscan` (`scan_ptr_id`);
ALTER TABLE `armored_cenzicreport` ADD CONSTRAINT `report_ptr_id_refs_id_c91eefff` FOREIGN KEY (`report_ptr_id`) REFERENCES `armored_report` (`id`);
CREATE TABLE `armored_cenzicvulnerability` (
    `vulnerability_ptr_id` integer NOT NULL PRIMARY KEY,
    `provider_id` integer NOT NULL UNIQUE,
    `family` longtext NOT NULL,
    `name` longtext NOT NULL,
    `description` longtext NOT NULL,
    `how_it_works` longtext NOT NULL,
    `impact` longtext NOT NULL,
    `solution` longtext NOT NULL,
    `risk` integer,
    `test_id` integer,
    `service` varchar(255) NOT NULL
)
;
ALTER TABLE `armored_cenzicvulnerability` ADD CONSTRAINT `vulnerability_ptr_id_refs_id_755d62f` FOREIGN KEY (`vulnerability_ptr_id`) REFERENCES `core_vulnerability` (`id`);
CREATE TABLE `armored_cenzicreference` (
    `reference_ptr_id` integer NOT NULL PRIMARY KEY,
    `mensagem` longtext NOT NULL,
    `data_criacao` datetime,
    `http_request` longtext NOT NULL,
    `http_response` longtext NOT NULL
)
;
ALTER TABLE `armored_cenzicreference` ADD CONSTRAINT `reference_ptr_id_refs_id_5e734483` FOREIGN KEY (`reference_ptr_id`) REFERENCES `core_reference` (`id`);
CREATE TABLE `armored_qualysarmoredscan` (
    `scan_ptr_id` integer NOT NULL PRIMARY KEY,
    `status` varchar(20) NOT NULL,
    `percentage` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `armored_qualysarmoredscan` ADD CONSTRAINT `scan_ptr_id_refs_id_9e393a37` FOREIGN KEY (`scan_ptr_id`) REFERENCES `core_scan` (`id`);
CREATE TABLE `armored_qualysreport` (
    `report_ptr_id` integer NOT NULL PRIMARY KEY,
    `scan_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `armored_qualysreport` ADD CONSTRAINT `scan_id_refs_scan_ptr_id_3759d811` FOREIGN KEY (`scan_id`) REFERENCES `armored_qualysarmoredscan` (`scan_ptr_id`);
ALTER TABLE `armored_qualysreport` ADD CONSTRAINT `report_ptr_id_refs_id_76fa163a` FOREIGN KEY (`report_ptr_id`) REFERENCES `armored_report` (`id`);
CREATE TABLE `armored_qualysvulnerability` (
    `vulnerability_ptr_id` integer NOT NULL PRIMARY KEY,
    `provider_id` integer NOT NULL UNIQUE,
    `category` varchar(200) NOT NULL,
    `last_update` datetime NOT NULL,
    `diagnosis` longtext,
    `consequence` longtext,
    `solution` longtext
)
;
ALTER TABLE `armored_qualysvulnerability` ADD CONSTRAINT `vulnerability_ptr_id_refs_id_519de4f2` FOREIGN KEY (`vulnerability_ptr_id`) REFERENCES `core_vulnerability` (`id`);
CREATE TABLE `armored_qualysreference` (
    `reference_ptr_id` integer NOT NULL PRIMARY KEY,
    `rid` varchar(765) NOT NULL,
    `description` longtext NOT NULL,
    `section` varchar(765) NOT NULL,
    `compliance_type` varchar(765) NOT NULL,
    `info` varchar(765) NOT NULL
)
;
ALTER TABLE `armored_qualysreference` ADD CONSTRAINT `reference_ptr_id_refs_id_900e223c` FOREIGN KEY (`reference_ptr_id`) REFERENCES `core_reference` (`id`);
CREATE INDEX `armored_reportvulnerability_29fa1030` ON `armored_reportvulnerability` (`report_id`);
CREATE INDEX `armored_reportvulnerability_43a42eb3` ON `armored_reportvulnerability` (`vulnerability_id`);
CREATE INDEX `armored_reportvulnerability_96efd03e` ON `armored_reportvulnerability` (`reference_id`);
CREATE INDEX `armored_armoredplancontract_5b7abc50` ON `armored_armoredplancontract` (`device_id`);
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
ALTER TABLE `malware_malwaredevice` ADD CONSTRAINT `device_ptr_id_refs_id_4ad5cb06` FOREIGN KEY (`device_ptr_id`) REFERENCES `core_device` (`id`);
CREATE TABLE `malware_malwareplanrange` (
    `planrange_ptr_id` integer NOT NULL PRIMARY KEY,
    `domain_quantity` integer UNSIGNED NOT NULL,
    `links_quantity` integer UNSIGNED NOT NULL
)
;
ALTER TABLE `malware_malwareplanrange` ADD CONSTRAINT `planrange_ptr_id_refs_id_d0887c36` FOREIGN KEY (`planrange_ptr_id`) REFERENCES `core_planrange` (`id`);
CREATE TABLE `malware_malwareplancontract` (
    `plancontract_ptr_id` integer NOT NULL PRIMARY KEY,
    `device_id` integer NOT NULL
)
;
ALTER TABLE `malware_malwareplancontract` ADD CONSTRAINT `plancontract_ptr_id_refs_id_c21e6df0` FOREIGN KEY (`plancontract_ptr_id`) REFERENCES `core_plancontract` (`id`);
ALTER TABLE `malware_malwareplancontract` ADD CONSTRAINT `device_id_refs_device_ptr_id_dac8576c` FOREIGN KEY (`device_id`) REFERENCES `malware_malwaredevice` (`device_ptr_id`);
CREATE TABLE `malware_malwareschedule` (
    `schedule_ptr_id` integer NOT NULL PRIMARY KEY,
    `device_id` integer NOT NULL
)
;
ALTER TABLE `malware_malwareschedule` ADD CONSTRAINT `schedule_ptr_id_refs_id_41033d84` FOREIGN KEY (`schedule_ptr_id`) REFERENCES `core_schedule` (`id`);
ALTER TABLE `malware_malwareschedule` ADD CONSTRAINT `device_id_refs_device_ptr_id_34ed0b2c` FOREIGN KEY (`device_id`) REFERENCES `malware_malwaredevice` (`device_ptr_id`);
CREATE TABLE `malware_hackalertmalwarescan` (
    `scan_ptr_id` integer NOT NULL PRIMARY KEY,
    `hackalert_id` integer
)
;
ALTER TABLE `malware_hackalertmalwarescan` ADD CONSTRAINT `scan_ptr_id_refs_id_a5dec6e6` FOREIGN KEY (`scan_ptr_id`) REFERENCES `core_scan` (`id`);
CREATE INDEX `malware_malwareplancontract_5b7abc50` ON `malware_malwareplancontract` (`device_id`);
CREATE INDEX `malware_malwareschedule_5b7abc50` ON `malware_malwareschedule` (`device_id`);
COMMIT;
