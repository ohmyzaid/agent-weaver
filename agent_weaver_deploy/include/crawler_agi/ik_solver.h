#ifndef CRAWLER_AGI_IK_SOLVER_H
#define CRAWLER_AGI_IK_SOLVER_H

namespace agent_weaver {
struct Point3D { float x, y, z; };
struct JointAngles { float coxia, femur, tibia; };
struct LegLengths { float coxia, femur, tibia; };

class IKSolver {
public:
    IKSolver();
    JointAngles solve(int leg_index, const Point3D& target) const;
};
}
#endif
