export enum AuthorityScope {
    SESSION = "SESSION",
    ENTITY = "ENTITY",
    GLOBAL = "GLOBAL"
}

export interface NeuroIRPacket {
    version: "1.0";
    instructionId: string;       
    entityId: string;            
    timestamp: number;           
    instructionType: "STATE_MUTATION" | "QUERY" | "POLICY_UPDATE";
    authorityScope: AuthorityScope;
    
    preconditions: {
        minTrust: number;
        requiredPermissions: string[];
    };
    
    delta: {
        target: string;          
        action: "INC" | "DEC" | "SET";
        value: any;
    };
    
    postconditions: {
        expectedStateHash: string;
    };
}
