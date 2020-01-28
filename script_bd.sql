-----mc-----------
CREATE TABLE mc(
mc_id bigint,
mc_dsc varchar(1024),
primary key(mc_id)
);

-----entity------
CREATE TABLE entity(
lc_id bigint,
lc_dsc varchar(1024),
mc_id bigint REFERENCES mc (mc_id),
primary key(lc_id)
);

-------- opportunity---------------
CREATE TABLE opportunity(
id bigInt,
title varchar(1024),
created_at timestamp,
available_openings bigint,
duration bigint,
subproduct varchar(1024),
product varchar(38),
host_lc bigint REFERENCES entity (lc_id),
host_mc bigint REFERENCES mc (mc_id),
primary key (id)
);

----------- applications----------
CREATE TABLE applications(
apl_seq bigserial, 
id_application bigint,
id_ep bigint,
id_opportunity bigint REFERENCES opportunity (id),
id_home bigint REFERENCES mc (mc_id),
id_host bigint REFERENCES mc (mc_id), 
lc_home bigint REFERENCES entity (lc_id),
product varchar(38), 
status varchar(38), 
applied_at varchar(38), 
accepted_at timestamp, 
approved_at timestamp, 
pred_realized_at timestamp,
realized_at timestamp,
finished_at timestamp,
completed_at timestamp, 
break_approval_at timestamp,
primary key (apl_seq)
);
--------- Standards ----------
CREATE TABLE standards(
std_seq bigserial,
id_application bigint,
std_1 varchar(38),
std_2 varchar(38),
std_3 varchar(38),
std_4 varchar(38),
std_5 varchar(38),
std_6 varchar(38),
std_7 varchar(38),
std_8 varchar(38),
std_9 varchar(38),
std_10 varchar(38),
std_11 varchar(38),
std_12 varchar(38),
std_13 varchar(38),
std_14 varchar(38),
std_15 varchar(38),
std_16 varchar(38),
date_std_1 timestamp,
date_std_2 timestamp,
date_std_3 timestamp,
date_std_4 timestamp,
date_std_5 timestamp,
date_std_6 timestamp,
date_std_7 timestamp,
date_std_8 timestamp,
date_std_9 timestamp,
date_std_10 timestamp,
date_std_11 timestamp,
date_std_12 timestamp,
date_std_13 timestamp,
date_std_14 timestamp,
date_std_15 timestamp,
date_std_16 timestamp,
primary key (std_seq)
);
-----------daal---------
CREATE TABLE daal(
reg_seq bigserial, 
application_id varchar(100),
ep_id varchar(100),
home_lc varchar(2048),
home_mc varchar(100),
home_region	varchar(100),
lc_alignment varchar(2048),
op_id bigint,
opp_title varchar(2048),
branch_name varchar(2048),
company_name varchar(2048),
product varchar(1024),
subproduct varchar(1024),
host_lc varchar(100),
host_mc varchar(100),
host_region varchar(100),
application_status varchar(38),
date_ep_signed_up timestamp, 
date_opportunity_created timestamp, 
date_applied timestamp,
date_accepted_rejected timestamp,
date_an_signed timestamp,
date_marked_paid timestamp,
date_approved timestamp,
date_realized timestamp,
date_finished timestamp,
date_opportunity_start timestamp,
date_opportunity_end timestamp,
active_member varchar(38),
role_dsc varchar(100),	
date_first_position_start timestamp,
date_lst_position_end timestamp,
sdg_goal varchar(100),
sdg_target varchar(2048),
ep_backgrouds varchar(2048),
primary key (reg_seq)
);

CREATE INDEX opportunity_id_idx on opportunity(id);
CREATE INDEX opportunity_host_lc_idx on opportunity(host_lc);
CREATE INDEX opportunity_host_mc_idx on opportunity(host_mc);
CREATE INDEX entity_mc_id_idx on entity(mc_id);
CREATE INDEX entity_lc_id_idx on entity(lc_id);
CREATE INDEX mc_mc_id_idx on mc(mc_id);
CREATE INDEX mc_mc_dsc_idx on mc(mc_dsc);
CREATE INDEX applications_id_application_idx on applications(id_application);
CREATE INDEX applications_apl_seq_idx on applications(apl_seq);
CREATE INDEX applications_id_opportunity_idx on applications(id_opportunity);
CREATE INDEX applications_id_home_idx on applications(id_home);
CREATE INDEX applications_id_host_idx on applications(id_host);
CREATE INDEX applications_lc_home_idx on applications(lc_home);
CREATE INDEX applications_product_idx on applications(product);
CREATE INDEX applications_status_idx on applications(status);
CREATE INDEX applications_applied_at_idx on applications(applied_at);
CREATE INDEX applications_accepted_at_idx on applications(accepted_at);
CREATE INDEX applications_approved_at_idx on applications(approved_at);
CREATE INDEX applications_realized_at_idx on applications(realized_at);
CREATE INDEX applications_completed_at_idx on applications(completed_at);
