#ifndef CombineTools_HhhSystematics_h
#define CombineTools_HhhSystematics_h
#include "CombineTools/interface/CombineHarvester.h"

namespace ch {

// Legacy SM analysis systematics
// Implemented in src/HttSystematics_SMLegacy.cc
void AddSystematics_hhh_et_mt(CombineHarvester& cb);
void AddSystematics_hhh_tt(CombineHarvester& cb);

// Legacy MSSM analysis systematics
// Implemented in src/HttSystematics_MSSMLegacy.cc
//void AddMSSMSystematics(CombineHarvester& cb);
}

#endif
