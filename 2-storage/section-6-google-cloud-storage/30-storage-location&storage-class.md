
# Storage Location

## Region (one region)

  - Lowest latency within a single region

  - Replicated data across multiple zones in a single region

## Dual-Region (2 regions)

  - High availability and low latency across 2 regions (Paired region)

  - Auto-failover

## Multi-region (more than two regions)

  - Highest availability across continent area - US,EU,Asia

  - Auto-failover


* NOTES:
  - Failover (BASED ON COMPUTE ENGINE DOCS): "

  With regional persistent disks, when the device is in replicating mode, data is automatically replicated to two zones in a region. A write is acknowledged back to a VM when it is durably persisted in both replicas.

  If replication to one zone fails or is very slow for a while, the disk switches to unreplicated mode. In this mode, write is acknowledged after it is durably persisted in one replica.

  "
# Storage Class

## Standard

  - good for hot data

  - high frequency acess

  - most expensive storage

  - access cost is very low

  - low latency

  - SLA:
    * 99.95% Multi/Dual
    * 99.9% Regional

## Near Line

  - Low frequency access once in 30 days

  - storage is cheaper than Standard

  - Access cost is higher

  - should be used as a Backup

  - SLA:
    * 99.9% Multi/Dual
    * 99.0% Regional

## Cold Line

  - Very low frequency to access

  - Once in 90 days access

  - Storage is cheaper than Near Line

  - SLA:
    * 99.9% Multi/Dual
    * 99.0% Regional

## Archive

  - offline data

  - long-term data preservation

  - Once in a year access

  - Storage is the Cheapest

  - Access cost is very high

  - no SLA

* NOTES:
  - SLA (Service Level Agreement): Monthly Uptime percentage.
