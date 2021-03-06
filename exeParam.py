# homemade
import campaign          as cp
import matrix            as cm
import algorithms        as cmm
import ScheduleManagment as sm
import setup             as s  
import pwa               as pwa

def main():
    # #######################################################################
    #                                                                       #
    #                PARAMETERS TO BE MODIFIED                              #
    #                                                                       #
    #               Modify the desired values                               #
    #               save py file (ctrl+s)                                   #
    #               then press F5 to execute   (if idle is used)                             #
    #                                                                       #
    # #######################################################################

    #Campaign title and name ==============================================
    campaignName         = "uni_test3d_m5_50n10_1000i_gamma_LDM"      # string
    campaignUser         = "FCO"            # string
    # Seed ================================================================
    seedForce            = None             # integer

    # Job Set size with N_NumberEnd >= N_NumberBegin ======================
    N_NumberBegin        = 10               # int
    N_NumberEnd          = 1000             # int
    # OR LIST OF JOBS Numbers (N_List has priority.  use N_NumberBegin and N_NumberEnd if  N_List = [])
    N_List               = []

    # Machines number with M_NumberEnd >= M_NumberBegin ===================
    M_NumberBegin        = 5                # int
    M_NumberEnd          = 50               # int
    # OR LIST OF JOBS Numbers (N_List has priority.  use M_NumberBegin and M_NumberEnd if  M_List = [])
    M_List               = []

    # Job set generation methods ===========================================
    matUniformNumber    = 0                 # int
    matNonUniformNumber = 0                 # int 
    matGammaNumber      = 1                 # int
    matBetaNumber       = 0                 # int
    matExponentialNumber= 0                 # int

    # From Parallel WorkLoad Archive ======================================
    # pwa.pwaFileChoice(X) if None asc you witch file to use eg pwa.pwaFileChoice()
    #                       if 1   use all files present in the PWA folder
    #                       if 0   does not use any of the files present   
    matRealFiles        = pwa.pwaFileChoice(0)

    # Properties of generation ============================================
    nAb                 = 1.0               # float
    nBb                 = 1000.0            # float
    nAlpah              = 1.0               # float for gamma (k) and beta (alpha)
    nBeta               = 1.0               # float for gamma (theta)
    nLambda             = 1.0               # float for exponential (lambda)

      #Algorithms ==========================================================
    useLPT              = 0                 # 1 or 0
    useSLACK            = 0                 # 1 or 0
    useLDM              = 1                 # 1 or 0
    useCOMBINE          = 0                 # 1 or 0
    useMULTIFIT         = 0                 # 1 or 0

    # #######################################################################
    #                                                                       #
    #                APPLICATION PART                                       #
    #                do not change anything here                            #
    #                                                                       #
    # #######################################################################

    #======================================================================
    # Parameters file (json)
    #======================================================================
    if s.EXP_PARAMETERS:
        fileSetup = s.ParamFile()
        fileSetup.create(campaignName,campaignUser,
                         seedForce,N_NumberBegin,N_NumberEnd,N_List, M_NumberBegin,M_NumberEnd, M_List,
                         matUniformNumber,matNonUniformNumber,matGammaNumber,matBetaNumber,matExponentialNumber,
                         matRealFiles,
                         nAb, nBb,nAlpah,nBeta,nLambda,
                         useLPT,useSLACK,useLDM,useCOMBINE,useMULTIFIT)
    print("===============================================================")
    print("Results computation                                            ")
    print("===============================================================")
    c = cp.Campaign(campaignName, campaignUser,
                    N_NumberBegin, N_NumberEnd, N_List,
                    M_NumberBegin, M_NumberEnd, M_List,
                    matUniformNumber,
                    matNonUniformNumber,
                    matGammaNumber,
                    matBetaNumber,
                    matExponentialNumber,
                    matRealFiles,
                    nAb,
                    nBb,
                    nAlpah,
                    nBeta,
                    nLambda,
                    seedForce)
    #
    if useLPT==1:      c.runAlgorithm(cmm.lpt)
    if useSLACK==1:    c.runAlgorithm(cmm.slack)
    if useLDM==1:      c.runAlgorithm(cmm.ldm)
    if useCOMBINE==1:  c.runAlgorithm(cmm.combine)
    if useMULTIFIT==1: c.runAlgorithm(cmm.multifit)
    c.exportCSV()

if __name__ == "__main__":
    main()
