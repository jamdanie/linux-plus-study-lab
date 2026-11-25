# When can the old address still appear?

In this simplified case a resolver caches an A record at 09:00:00 with a TTL of 120 seconds. The authoritative record changes 30 seconds later. The resolver keeps its original entry until expiry. Ignore prefetching and stale-answer features for this exercise.

```bash
for elapsed in 30 90 120; do
  remaining=$((120 - elapsed))
  printf '%s seconds since lookup: %s seconds left\n' "$elapsed" "$remaining"
done
```

Predict the old entry's remaining TTL at 09:01:30. You should get 30 seconds. At 09:02:00 the original TTL has expired; the next query needs fresh resolution in this model. This clock starts when the resolver cached the old record. Changing the authoritative value doesn't restart that clock.

**Challenge.** A second resolver first cached the old record at 09:00:20. When does its entry expire? At 09:02:20. Two clients using different resolvers can briefly receive different valid cached answers. Record the resolver and time alongside each observation.
