# Talon.one writer

## What It Does

This writer sends measured data objects to Talon.one system.

https://developers.talon.one/Tutorials-and-Guides/How-do-I-transfer-my-existing-coupon-codes

### Allowed data objects to write

- CSV file

#### input.csv

Represents collected raw coupon data in format below:

["value","expirydate","startdate","recipientintegrationid","limitval","attributes"]

Note that only the **value** column is required. All others are optional. Limits default to 1 if they are not provided.
The structure of a coupon import CSV file is using ISO8601 for dates. 

- value: Id of the specific coupon, Id is unique
- expirydate: Timestamp YYYY-MM-DDTHH:mm:ssZ
- startdate: Timestamp YYYY-MM-DDTHH:mm:ssZ
- recipientintegrationid: customer Id
- limitval: is integer, default 1
- attributes: format example: "{""Key1"": ""value"", ""Key2"": ""value""}"

**Input table must be named \"input.csv\"**

## Configuration


### Parameters

from endpoint
https://example.talon.one/v1/applications/42/campaigns/3/import_coupons

<pre>
{
  "project": "<example>",
  "application-id": <id>,
  "campaign-id": <id>,
  "#bearer": "$YOUR_TOKEN"
}
</pre>


- `endpoint` is an endpoint of the service
- `#bearer` is your secret token
- `project` is your name of organization
- `application-id` is your application id
- `campaign-id` is your campaign id


## Contact

BizzTreat, s.r.o
Řehořova 968/42
Prague

If you have any question contact support@bizztreat.com

Cheers!
