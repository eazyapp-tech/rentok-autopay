# The queries behind the numbers (17 Sep 2026)

Run against RentOk's production database through Metabase (database id 2, "prod db rentOk"). Each query says what it was used for. Tenant status 1 is read as "active"; that reading is not confirmed with engineering.

## Rent spread of active tenants

Used for: the median rent of ₹8,250, and the share of tenants above ₹15,000.

```sql
select count(*) n,
 percentile_cont(array[0.25,0.5,0.75,0.9]) within group (order by rent_amount) pcts,
 round(100.0*avg((rent_amount<=2000)::int),1) le2k,
 round(100.0*avg((rent_amount>2000 and rent_amount<=10000)::int),1) to10k,
 round(100.0*avg((rent_amount>10000 and rent_amount<=15000)::int),1) to15k,
 round(100.0*avg((rent_amount>15000 and rent_amount<=25000)::int),1) to25k,
 round(100.0*avg((rent_amount>25000)::int),1) over25k
from tenant where status=1 and rent_amount>0 and rent_amount<500000;
```

Result: 348,071 tenants. Quartiles ₹5,700, ₹8,250, ₹13,000 and ₹18,250. Bands: 3.9% at ₹2,000 or less, 59.6% to ₹10,000, 20.6% to ₹15,000, 10.7% to ₹25,000, 5.2% above.

## Autopay mandates by status

Used for: the starting count, and the mandates left on tenants who have left (#7005).

```sql
select status, count(*) n, count(distinct tenant_id) tenants, max(created_at) latest
from autopay group by 1 order by 2 desc;

select t.status, a.payment_method_type, count(distinct a.tenant_id) tenants,
       sum((a.plan_amount>15000)::int) above15k
from autopay a join tenant t on t.id::text = a.tenant_id::text
where a.status='active' group by 1,2 order by 3 desc;
```

Result: 1,282 active mandate rows, of which 778 belong to current tenants (768 UPI, 8 e-NACH, 2 with no method). 1,348 tenants started and never finished; 437 cancelled themselves; 78 are waiting on bank approval; 66 paused.

## Online payments, and the shape of the month

Used for: 141,798 online payments in 30 days, the average of ₹10,748, and the pattern by day of month.

```sql
select payment_mode, count(*) n, round(avg(net_amount)) avg_amt,
       sum((net_amount>2000)::int) above2k
from payments
where paid_date >= now() - interval '30 days' and is_active=1
group by 1 order by 2 desc;

select extract(day from paid_date at time zone 'Asia/Kolkata')::int d, count(*) n
from payments
where payment_mode=205 and is_active=1
  and paid_date >= '2026-08-01' and paid_date < '2026-09-01'
group by 1 order by 1;
```

Payment mode 205 is payment through RentOk online, and it includes Autopay debits. Modes 2040 to 2048 are payments recorded by hand, such as cash.

Result: 18,049 online payments on 1 August, 42,284 over the 2nd to the 5th, and 27,142 over the 17th to the 31st.

## New tenants per week

Used for: about 1,300 new tenants a day.

```sql
select date_trunc('week', "createdAt")::date wk, count(*) new_tenants
from tenant
where "createdAt" >= now() - interval '8 weeks' and status=1
group by 1 order by 1;
```

Result: about 9,000 a week over the last 8 weeks.

## How often tenants are billed

Used for: the tenants who do not pay monthly.

```sql
select coalesce(rental_frequency::text,'null') f, count(*)
from tenant where status=1 group by 1 order by 2 desc;
```

The meaning of each code is not confirmed. A review read it as about 9,500 tenants on quarterly, yearly or manual schedules.
