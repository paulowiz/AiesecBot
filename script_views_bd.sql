-----------VIEWS---------

-----all_application-----
create or replace view all_application AS 
SELECT DISTINCT apl.id_application,
    apl.status,
    apl.product,
    apl.id_ep,
    apl.id_opportunity,
    opp.title,
    opp.created_at,
    opp.available_openings,
    opp.duration,
    ent.lc_dsc AS lc_host,
    mc_host.mc_dsc AS mc_host,
    ent_home.lc_dsc AS lc_home,
    mc_home.mc_dsc AS mc_home,
    to_char(apl.applied_at, 'YYYY-MM-DD'::text) AS applied_at,
    to_char(apl.accepted_at, 'YYYY-MM-DD'::text) AS accepted_at, 
    to_char(apl.approved_at, 'YYYY-MM-DD'::text) AS approved_at,
    to_char(apl.pred_realized_at, 'YYYY-MM-DD'::text) AS pred_realized_at,
    to_char(apl.realized_at, 'YYYY-MM-DD'::text) AS realized_at,
    to_char(apl.finished_at, 'YYYY-MM-DD'::text) AS finished_at,
    to_char(apl.completed_at, 'YYYY-MM-DD'::text) AS completed_at,
    to_char(apl.break_approval_at, 'YYYY-MM-DD'::text) AS break_approval_at
   FROM applications apl
     JOIN opportunity opp ON opp.id = apl.id_opportunity
     JOIN entity ent ON ent.lc_id = opp.host_lc
     JOIN entity ent_home ON ent_home.lc_id = apl.lc_home
     JOIN mc mc_home ON mc_home.mc_id = apl.id_home
     JOIN mc mc_host ON mc_host.mc_id = apl.id_host;


----analitics_aiesec--------
create or replace view analitics_aiesec AS 
 SELECT DISTINCT apl.id_application,
    apl.status,
    apl.product,
    apl.id_ep,
    apl.id_opportunity,
    opp.title,
    opp.created_at,
    opp.available_openings,
    opp.duration,
    ent.lc_dsc AS lc_host,
    mc_host.mc_dsc AS mc_host,
    ent_home.lc_dsc AS lc_home,
    mc_home.mc_dsc AS mc_home,
    to_char(apl.applied_at, 'YYYY-MM-DD'::text) AS applied_at,
    to_char(apl.accepted_at, 'YYYY-MM-DD'::text) AS accepted_at,
    to_char(apl.approved_at, 'YYYY-MM-DD'::text) AS approved_at,
    to_char(apl.pred_realized_at, 'YYYY-MM-DD'::text) AS pred_realized_at,
    to_char(apl.realized_at, 'YYYY-MM-DD'::text) AS realized_at,
    to_char(apl.finished_at, 'YYYY-MM-DD'::text) AS finished_at,
    to_char(apl.completed_at, 'YYYY-MM-DD'::text) AS completed_at,
    to_char(apl.break_approval_at, 'YYYY-MM-DD'::text) AS break_approval_at
   FROM applications apl
     JOIN opportunity opp ON opp.id = apl.id_opportunity
     JOIN entity ent ON ent.lc_id = opp.host_lc
     JOIN entity ent_home ON ent_home.lc_id = apl.lc_home
     JOIN mc mc_home ON mc_home.mc_id = apl.id_home
     JOIN mc mc_host ON mc_host.mc_id = apl.id_host;

--E2E_APPLICATION---
create or replace view e2e_application as
SELECT master.mc_home,
    master.lc_home,
    master.mc_host,
    master.lc_host,
    to_date(master.applied_at::text, 'YYYY-MM-DD'::text) AS applied_at,
    master.product,
    master.qtd
   FROM ( SELECT all_application.lc_home,
            all_application.lc_host,
            all_application.mc_home,
            all_application.mc_host,
            all_application.applied_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.applied_at IS NOT NULL
          GROUP BY all_application.lc_home, all_application.lc_host, all_application.mc_home, all_application.mc_host, all_application.applied_at, all_application.product
          ORDER BY all_application.applied_at DESC) master;

--ICX_ACCEPTED--
create or replace view icx_accepted as 
 SELECT master.lc_host,
    to_date(master.accepted_at, 'YYYY-MM-DD'::text) AS accepted_at,
    master.product,
    master.qtd,
    'accepted'::text AS status
   FROM ( SELECT all_application.lc_host,
            all_application.accepted_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_host::text = 'Brazil'::text AND all_application.accepted_at IS NOT NULL
          GROUP BY all_application.lc_host, all_application.accepted_at, all_application.product
          ORDER BY all_application.accepted_at DESC) master;

--ICX_APPLIED--
create or replace view icx_applied as 
 SELECT master.lc_host,
    to_date(master.applied_at::text, 'YYYY-MM-DD'::text) AS applied_at,
    master.product,
    master.qtd,
    'applied'::text AS status
   FROM ( SELECT all_application.lc_host,
            all_application.applied_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_host::text = 'Brazil'::text AND all_application.applied_at IS NOT NULL
          GROUP BY all_application.lc_host, all_application.applied_at, all_application.product
          ORDER BY all_application.applied_at DESC) master;

--ICX_ACCEPTED--
create or replace view icx_accepted as 
 SELECT master.lc_host,
    to_date(master.accepted_at, 'YYYY-MM-DD'::text) AS accepted_at,
    master.product,
    master.qtd,
    'accepted'::text AS status
   FROM ( SELECT all_application.lc_host,
            all_application.accepted_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_host::text = 'Brazil'::text AND all_application.accepted_at IS NOT NULL
          GROUP BY all_application.lc_host, all_application.accepted_at, all_application.product
          ORDER BY all_application.accepted_at DESC) master;

--ICX_APPROVED--
create or replace view icx_approved as 
 SELECT master.lc_host,
    to_date(master.approved_at, 'YYYY-MM-DD'::text) AS approved_at,
    master.product,
    master.qtd,
    'approved'::text AS status
   FROM ( SELECT all_application.lc_host,
            all_application.approved_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_host::text = 'Brazil'::text AND all_application.approved_at IS NOT NULL
          GROUP BY all_application.lc_host, all_application.approved_at, all_application.product
          ORDER BY all_application.approved_at DESC) master;

--ICX_COMPLETED--
create or replace view icx_completed as 
 SELECT master.lc_host,
    to_date(master.completed_at, 'YYYY-MM-DD'::text) AS completed_at,
    master.product,
    master.qtd,
    'completed'::text AS status
   FROM ( SELECT all_application.lc_host,
            all_application.completed_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_host::text = 'Brazil'::text AND all_application.completed_at IS NOT NULL
          GROUP BY all_application.lc_host, all_application.completed_at, all_application.product
          ORDER BY all_application.completed_at DESC) master;

--ICX_FINISHED--
create or replace view icx_finished as 
 SELECT master.lc_host,
    to_date(master.finished_at, 'YYYY-MM-DD'::text) AS finished_at,
    master.product,
    master.qtd,
    'finished'::text AS status
   FROM ( SELECT all_application.lc_host,
            all_application.finished_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_host::text = 'Brazil'::text AND all_application.finished_at IS NOT NULL
          GROUP BY all_application.lc_host, all_application.finished_at, all_application.product
          ORDER BY all_application.finished_at DESC) master;

--ICX_PRED_REALIZED--
create or replace view icx_pred_realized as 
 SELECT master.lc_host,
    to_date(master.pred_realized_at, 'YYYY-MM-DD'::text) AS pred_realized_at,
    master.product,
    master.qtd,
    'pred_realized'::text AS status
   FROM ( SELECT all_application.lc_host,
            all_application.pred_realized_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_host::text = 'Brazil'::text AND all_application.pred_realized_at IS NOT NULL
          GROUP BY all_application.lc_host, all_application.pred_realized_at, all_application.product
          ORDER BY all_application.pred_realized_at DESC) master;

--ICX_REALIZED--
create or replace view icx_realized as 
 SELECT master.lc_host,
    to_date(master.realized_at, 'YYYY-MM-DD'::text) AS realized_at,
    master.product,
    master.qtd,
    'realized'::text AS status
   FROM ( SELECT all_application.lc_host,
            all_application.realized_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_host::text = 'Brazil'::text AND all_application.realized_at IS NOT NULL
          GROUP BY all_application.lc_host, all_application.realized_at, all_application.product
          ORDER BY all_application.realized_at DESC) master;

--ICX_CENTRAL--
create or replace view icx_central as 
 SELECT master.lc_host,
    master.approved_at AS data,
    master.product,
    master.qtd,
    master.status
   FROM ( SELECT icx_approved.lc_host,
            icx_approved.approved_at,
            icx_approved.product,
            icx_approved.qtd,
            icx_approved.status
           FROM icx_approved
        UNION
         SELECT icx_applied.lc_host,
            icx_applied.applied_at,
            icx_applied.product,
            icx_applied.qtd,
            icx_applied.status
           FROM icx_applied
        UNION
         SELECT icx_accepted.lc_host,
            icx_accepted.accepted_at,
            icx_accepted.product,
            icx_accepted.qtd,
            icx_accepted.status
           FROM icx_accepted
        UNION
         SELECT icx_realized.lc_host,
            icx_realized.realized_at,
            icx_realized.product,
            icx_realized.qtd,
            icx_realized.status
           FROM icx_realized
        UNION
         SELECT icx_finished.lc_host,
            icx_finished.finished_at,
            icx_finished.product,
            icx_finished.qtd,
            icx_finished.status
           FROM icx_finished
        UNION
         SELECT icx_completed.lc_host,
            icx_completed.completed_at,
            icx_completed.product,
            icx_completed.qtd,
            icx_completed.status
           FROM icx_completed) master;



--OGX_APPLIED--
create or replace view ogx_applied as
 SELECT master.lc_home,
    to_date(master.applied_at::text, 'YYYY-MM-DD'::text) AS applied_at,
    master.product,
    master.qtd,
    'applied'::text AS status
   FROM ( SELECT all_application.lc_home,
            all_application.applied_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_home::text = 'Brazil'::text AND all_application.applied_at IS NOT NULL
          GROUP BY all_application.lc_home, all_application.applied_at, all_application.product
          ORDER BY all_application.applied_at DESC) master;

--OGX_ACCEPTED--
create or replace view ogx_accepted as
 SELECT master.lc_home,
    to_date(master.accepted_at, 'YYYY-MM-DD'::text) AS accepted_at,
    master.product,
    master.qtd,
    'accepted'::text AS status
   FROM ( SELECT all_application.lc_home,
            all_application.accepted_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_home::text = 'Brazil'::text AND all_application.accepted_at IS NOT NULL
          GROUP BY all_application.lc_home, all_application.accepted_at, all_application.product
          ORDER BY all_application.accepted_at DESC) master;


--OGX_APPROVED--
create or replace view ogx_approved as
 SELECT master.lc_home,
    to_date(master.approved_at, 'YYYY-MM-DD'::text) AS approved_at,
    master.product,
    master.qtd,
    'approved'::text AS status
   FROM ( SELECT all_application.lc_home,
            all_application.approved_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_home::text = 'Brazil'::text AND all_application.approved_at IS NOT NULL
          GROUP BY all_application.lc_home, all_application.approved_at, all_application.product
          ORDER BY all_application.approved_at DESC) master;

--OGX_COMPLETED--
create or replace view ogx_completed as
 SELECT master.lc_home,
    to_date(master.completed_at, 'YYYY-MM-DD'::text) AS completed_at,
    master.product,
    master.qtd,
    'completed'::text AS status
   FROM ( SELECT all_application.lc_home,
            all_application.completed_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_home::text = 'Brazil'::text AND all_application.completed_at IS NOT NULL
          GROUP BY all_application.lc_home, all_application.completed_at, all_application.product
          ORDER BY all_application.completed_at DESC) master;

--OGX_FINISHED--
create or replace view ogx_finished as
 SELECT master.lc_home,
    to_date(master.finished_at, 'YYYY-MM-DD'::text) AS finished_at,
    master.product,
    master.qtd,
    'finished'::text AS status
   FROM ( SELECT all_application.lc_home,
            all_application.finished_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_home::text = 'Brazil'::text AND all_application.finished_at IS NOT NULL
          GROUP BY all_application.lc_home, all_application.finished_at, all_application.product
          ORDER BY all_application.finished_at DESC) master;

--OGX_PRED_REALIZED--
create or replace view ogx_pred_realized as
 SELECT master.lc_home,
    to_date(master.pred_realized_at, 'YYYY-MM-DD'::text) AS pred_realized_at,
    master.product,
    master.qtd,
    'pred_realized'::text AS status
   FROM ( SELECT all_application.lc_home,
            all_application.pred_realized_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_home::text = 'Brazil'::text AND all_application.pred_realized_at IS NOT NULL
          GROUP BY all_application.lc_home, all_application.pred_realized_at, all_application.product
          ORDER BY all_application.pred_realized_at DESC) master;

--OCX_REALIZED--
create or replace view ogx_realized as
 SELECT master.lc_home,
    to_date(master.realized_at, 'YYYY-MM-DD'::text) AS realized_at,
    master.product,
    master.qtd,
    'realized'::text AS status
   FROM ( SELECT all_application.lc_home,
            all_application.realized_at,
            all_application.product,
            count(*) AS qtd
           FROM all_application
          WHERE all_application.mc_home::text = 'Brazil'::text AND all_application.realized_at IS NOT NULL
          GROUP BY all_application.lc_home, all_application.realized_at, all_application.product
          ORDER BY all_application.realized_at DESC) master;

--OGX_CENTRAL--
create or replace view ogx_central as
 SELECT master.lc_home,
    master.approved_at AS data,
    master.product,
    master.qtd,
    master.status
   FROM ( SELECT ogx_approved.lc_home,
            ogx_approved.approved_at,
            ogx_approved.product,
            ogx_approved.qtd,
            ogx_approved.status
           FROM ogx_approved
        UNION
         SELECT ogx_applied.lc_home,
            ogx_applied.applied_at,
            ogx_applied.product,
            ogx_applied.qtd,
            ogx_applied.status
           FROM ogx_applied
        UNION
         SELECT ogx_accepted.lc_home,
            ogx_accepted.accepted_at,
            ogx_accepted.product,
            ogx_accepted.qtd,
            ogx_accepted.status
           FROM ogx_accepted
        UNION
         SELECT ogx_realized.lc_home,
            ogx_realized.realized_at,
            ogx_realized.product,
            ogx_realized.qtd,
            ogx_realized.status
           FROM ogx_realized
        UNION
         SELECT ogx_finished.lc_home,
            ogx_finished.finished_at,
            ogx_finished.product,
            ogx_finished.qtd,
            ogx_finished.status
           FROM ogx_finished
        UNION
         SELECT ogx_completed.lc_home,
            ogx_completed.completed_at,
            ogx_completed.product,
            ogx_completed.qtd,
            ogx_completed.status
           FROM ogx_completed) master;