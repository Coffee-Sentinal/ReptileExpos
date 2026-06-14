export type ConfidenceLevel='unknown'|'low'|'medium'|'high'; export type RiskLevel='low'|'medium'|'high'|'critical';
export interface Venue{name:string;city:string;country:string;region:string;latitude:number;longitude:number}
export interface EventDate{id:string;startDate:string;endDate:string;label:string}
export interface Event{id:string;name:string;venue:Venue;officialUrl:string;eventDates:EventDate[];knownFrequency:string;monitoringPriority:RiskLevel;confidence:ConfidenceLevel;description:string;isPlaceholder:boolean;sourceType:string}
export interface Website{id:string;name:string;url:string;type:string;notes:string;confidence:ConfidenceLevel;lastCheckedDate:string;publicSafe:boolean}
export interface EventWebsite{id:string;eventId:string;websiteId:string}
export interface Taxon{id:string;scientificName:string;commonName:string;taxonGroup:string;citesAppendix:string;euAnnex:string;nativeRangeCountries:string[];possibleOriginCountries:string[];transitCountries:string[];reasonForInclusion:string;evidenceBasis:string;confidence:ConfidenceLevel;identificationNotes:string}
export interface EventTaxon{id:string;eventId:string;taxonId:string;reasonForInclusion:string;evidenceBasis:string;confidence:ConfidenceLevel}
export interface EvidenceItem{id:string;title:string;evidenceType:string;url?:string|null;dateObserved:string;datePosted?:string|null;relatedEventId:string;relatedTaxaIds:string[];summary:string;extractedRedFlags:string[];analystNotes:string;confidence:ConfidenceLevel;publicSafeStatus:string}
export interface Airport{id:string;iata:string;name:string;city:string;country:string;latitude:number;longitude:number;eventIds:string[]}
export interface RouteRisk{id:string;eventId:string;direction:'inbound'|'outbound';originCountry:string;originRegion:string;transitHubCountry?:string;destinationAirportId:string;destinationCity:string;relevantTaxaIds:string[];timingWindowStart:string;timingWindowEnd:string;rationale:string;confidence:ConfidenceLevel;caveat:string}
export interface RiskScore{speciesRisk:number;onlineSignalRisk:number;courierLinkageRisk:number;inboundRouteRisk:number;outboundRouteRisk:number;seizureReportRisk:number;paperworkRisk:number;overallScore:number;monitoringPriority:RiskLevel;confidence:ConfidenceLevel;explanation:string[]}
export interface MonitoringWindow{key:string;label:string;start:string;end:string;status:'past'|'active'|'upcoming'}
export interface LeadPackage{id:string;eventId:string;title:string;html:string;caveat:string}
export interface Country{id:string;name:string;region:string}
