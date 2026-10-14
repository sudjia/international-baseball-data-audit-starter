# Baseball context for this audit

- **International amateur signing:** a regulatory category, not simply anyone born outside the US. Birthplace, citizenship, residence and signing eligibility can differ. Do not classify eligibility from Country/birthCountry alone.
- **J2:** the source's historical international-amateur market label. Signing calendars have changed; this label doesn't establish an exact July 2 signing date.
- **Prospect board:** an editorial/scouting selection. Players not listed can still be signed or playing. Never use board players as all-signee denominators.
- **Organization versus team:** a signing organization, board affiliation and performance team can differ after trades or assignments. Don't silently substitute one.
- **Level:** minor-league competition context. A comma-separated level string may describe multiple levels, not one observation suitable for level-specific comparisons.
- **Season and age:** distinguish board year, performance year and retrieval time. Current age isn't historical age. A signing year alone doesn't determine exact age at signing.
- **Bonus:** reported amount, not verified total organizational spending. Missing amount isn't zero; units/currency and disclosure source need confirmation.
- **FV / scouting grades:** assessments whose scale and interpretation need source documentation. They are not realized dollar values or a causal payoff from signing spend.
- **PA versus AB:** plate appearances are broader opportunities than at-bats. Different batting rates have different denominators; don't divide everything by AB. OBP/SLG/OPS are not automatically park/league/age-adjusted talent.
- **Rehab players:** MLB players can appear in minor-league peer data temporarily. Opportunity and age context matter.
- **Missing performance or debut:** may reflect coverage, timing or source behavior, not a known career failure. Estimating progression requires a complete cohort and follow-up, neither supplied by the selected board.

Ask your mentor when a baseball interpretation changes the population or meaning of a metric. Your engineering strengths—units, experimental design, uncertainty and traceability—are valuable here. This project doesn't require pretending to be a scout or making player-value predictions.
