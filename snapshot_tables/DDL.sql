
Table user_id {
  user_id varchar [primary key]
}

Table event_data {
  id integer [primary key]
  event_timestamp timestamp
  user_id integer
  event_name varchar
}

Table deposit {
  id integer [primary key]
  event_timestamp timestamp
  user_id integer
  amount float
  currency VARCHAR
  tx_status VARCHAR
}

Table withdrawal {
  id integer [primary key]
  event_timestamp timestamp
  user_id integer
  amount float
  interface VARCHAR
  currency VARCHAR
  tx_status VARCHAR
}



Ref: user_id.user_id < withdrawal.user_id // many-to-one
Ref: user_id.user_id < deposit.user_id // many-to-one
Ref: user_id.user_id < event_data.user_id // many-to-one