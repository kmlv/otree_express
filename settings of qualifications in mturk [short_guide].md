# Key points for mturk and qualifications
 :grin: :relieved: :mortar_board: :memo: :grin: :relieved: :mortar_board: :memo: :grin: :relieved: :mortar_board: :memo:
===================
## About wait pages in mturk
One issue is the risk that some players will drop out.
To partly remedy this, you should set timeout_seconds on each page, so that the page will be auto-submitted if the participant drops out or does not complete the page in time.
This way, players will not get stuck waiting for someone who dropped out.

## About points and real money in mturk
You can use money language in your app without impact the payment (if the player wins $40 doesn't imply you have to pay $40 )
Only set in real_world_currency_per_point: 

```
SESSION_CONFIG_DEFAULTS = {
'real_world_currency_per_point': 0.01,
'participation_fee': 1.00,
'num_bots': 6,
'doc': "",
'mturk_hit_settings': mturk_hit_settings,
}
```

##About qualifications in mturk
- [x] **First you have to create New QualificationType**

Go to Manage option in your mturk account. Then go to qualifications and click on "create New qualification type"
You have to do this for sandbox and for realmturk (you will have 2 ID)
(sandbox)

``` grant_qualification_id : 3LQV637WQB4JX22NPA62LG08IF76BE ```

(real mturk)

``` grant_qualification_id : 3X03PXFE93BZZPK7U8HT29SECH8OFF ```

- [x] **Second, you have to modify some settings for qualifications**

``` qualification.LocaleRequirement("EqualTo", "US"), ```
	 
Description:	The Location Qualification represents the location you specified with your mailing address. 
Some HITs may only be available to residents of particular countries, states, provinces or cities.

```qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),```
	
Description:	This Qualification is generated automatically and reflects the percentage of HITs for which 
you have submitted an answer that has been approved divided by the total number of HITs that have been approved or rejected. 
Your score is a value between 0 and 100. A score of 100 indicates that every HIT you have submitted has been approved.
	
```qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),```
	
Description:	This Qualification is generated automatically and reflects the number of HITs which you have submitted an answer that has been approved.
Your score is a value greater than or equal to 0.

```qualification.Requirement('3LQV637WQB4JX22NPA62LG08IF76BE', 'DoesNotExist')```

You have to put the same ID from the first line. 
Attach the Qualification as a QualificationRequirement to the new HIT using the "DoesNotExist" comparator.
With this method, previous workers will not be able to complete the new HIT and new workers simply need to accept the HIT in order to complete it.

- [x] **Third, you have assign Qualifications**

This is only necessary if you know the ID of specific workers , so in that case you have to create a vector of id_workers 
Example:

``` 
w <- c('Worker1','Worker2','etc.') # a vector containing WorkerIds
	AssignQualification(
	qual = thenewqual$QualificationTypeId,
	workers = w,
	values = "50")
```
			
- [x] **Fourth, create a new mturk session of the app (sandbox or real mturk) and spread your HIT to the world**
