# Initial dictionary: schema facts versus unresolved meaning

These are schema observations from discovery, not certified definitions or a cleaned model. Add observed types, missing conventions, transformations and evidence from **your own input**. Preserve source field names/case; do not rename without a mapping.

## Selected Tigers route: MLB biographies and hitting records

| Response / field | Observed representation | Interpretation / caution |
|---|---|---|
| people / id | Integer | MLBAM person ID; retain namespace, check uniqueness |
| birthDate | ISO string | Official API-reported DOB; agreement is not independent proof of accuracy |
| birthCountry | String | Birthplace country, not eligibility or citizenship |
| mlbDebutDate | ISO string or absent | Returned debut field when available; absence isn't a known negative outcome |
| currentAge | Integer | Current age; do not use for historical peers |
| splits / player.id | Integer | Person key, not necessarily unique across teams/seasons/levels |
| season | String | Requested observation season; compare to source block/type |
| team.id / league.id / sport.id | Integer | Observation metadata; current affiliation and full-season ownership can differ |
| stat.age | Integer | Reported season age; convention requires verification |
| stat.plateAppearances / atBats / hits | Numeric | Opportunity/counts; zero denominator makes some rates undefined |
| stat.baseOnBalls / strikeOuts / homeRuns | Numeric | Counts; aggregate numerators/denominators at a declared grain |
| stat.obp / slg / ops / avg | Formatted strings | Convert deliberately; sentinel strings aren't observed numeric rates |
| numTeams | Integer, when returned | Warns an aggregate may span teams; displayed team alone is insufficient |
| stats block / totalSplits | Integer | Expected response row count for pagination, not a census certificate |

## Optional later FanGraphs project (not required)

| Array / field | Observed representation | Safe interpretation / status |
|---|---|---|
| dataScout / UPID | String or missing | Source bridge identifier; verify completeness/uniqueness within board before use |
| PlayerId | String | Alternate source ID; relationship to other namespaces unverified |
| minorMasterId | String | Alternate minor identity field; not interchangeable by assumption |
| Signed_Yr | Integer | Reported signing year; not a date or precise signing age |
| Signed_Mkt | String | Source market category; J2 is the primary selected category |
| Signed_Org | String | Source-reported signing organization; independently verifying original organization is a separate task |
| Sign_Bonus | Integer or null | Reported bonus value; units/currency and complete contract interpretation unresolved |
| Country | String or missing | Source country label; birthplace/nationality/scouting-market semantics unresolved |
| Position | String | Board position; may differ from later playing position |
| Team | String | Board organization; not signing organization |
| Season | Integer | Scouting-board year for this array; do not replace with performance year |
| Age | Numeric-looking string | Board age; not signing age, convention unresolved |
| BirthDate | Numeric-looking string | Candidate spreadsheet serial; conversion/epoch and cross-source agreement need validation |
| FV_Current | Grade | Source scouting assessment; ordinal interpretation requires source documentation, not dollar valuation |
| dataStats / UPID | String | Candidate bridge to scouting; verify grain/cardinality and missing IDs |
| xMLBAMID | Integer | MLBAM bridge identifier; preserve as a namespace-labelled ID/string when storing |
| minormasterid | Integer | Different case/representation from scout field; do not assume equivalence without checking |
| Season | Integer | Batting performance year, distinct from scouting year |
| level | String | May contain multiple comma-separated levels; not necessarily a single player-level row |
| AffAbbName | String | Performance affiliation label; aggregation meaning needs validation |
| PA / AB / H / HR / BB / SO / G | Numeric | Batting opportunity/counts; confirm measurement and aggregation scope |
| AVG / OBP / SLG / OPS / wRC+ | Numeric | Source rates/context metrics; definitions and cross-level aggregation require documentation |
| Age | Numeric | Performance-source age; don't equate to scout age or current age automatically |

Exact signing date and confirmed signing nationality/eligibility are **not supplied as verified fields**. An absent column has no row-level missingness denominator. Never substitute cBonus, current Team or Country for the needed concept without evidence.

Candidate scout key is board year + UPID only for identified, validated records; missing IDs need a separate review path. Candidate stats grain is player-performance-season aggregate; verify rather than enforce assumed uniqueness. A bridge identifies a person, not the date or level of an observation.

## Henry's additions (complete as you work)

| Source table | One row means… | Proposed key and validation | Observed type/missing convention | Transformation + reason | Definition evidence / unresolved question |
|---|---|---|---|---|---|
| Your table | To fill | To fill | To fill | To fill | To fill |

For each derived metric add its population, numerator/denominator, units, missing treatment and aggregation grain. Record unresolved meanings explicitly rather than inventing them. Keep discovery findings/answers outside this learner dictionary.
