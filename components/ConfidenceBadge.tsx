import type {ConfidenceLevel} from '@/lib/types';
export default function ConfidenceBadge({level}:{level:ConfidenceLevel}){return <span className="rounded-full border border-cyan/30 bg-cyan/10 px-2 py-1 text-xs text-cyan">confidence: {level}</span>}
