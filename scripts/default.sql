ALTER ROLE cassandra WITH PASSWORD='SomeNonsenseThatNoOneWillThinkOf'
    AND SUPERUSER=false;

CREATE KEYSPACE IF NOT EXISTS profile WITH REPLICATION = { 'class' : 'NetworkTopologyStrategy', 'datacenter1' : 3 };
