CREATE TYPE status AS ENUM (
  'pending',
  'running',
  'succeeded',
  'cancelled',
  'failed'
);

CREATE TABLE tasks (
  id UUID PRIMARY KEY,
  data JSONB,
  status STATUS,
  created TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
